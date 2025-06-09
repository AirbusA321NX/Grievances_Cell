from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from Grievances import crud, schemas, models
from User.models import User
from database import get_db
from dependencies import get_current_active_user, RoleChecker
from roles import RoleEnum

# Role-based dependencies
admin_only = RoleChecker([RoleEnum.admin, RoleEnum.super_admin])
user_only  = RoleChecker([RoleEnum.user])
emp_only   = RoleChecker([RoleEnum.employee])

router = APIRouter(prefix="/grievances", tags=["Grievances"])

@router.post("/", response_model=schemas.GrievanceOut)
def create_grievance(
    grievance: schemas.GrievanceCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(user_only),
):
    # Only users can raise grievances
    return crud.create_grievance(db, grievance, current_user.id)

@router.get("/", response_model=List[schemas.GrievanceOut])
def read_grievances(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user),
):
    if current_user.role == RoleEnum.user:
        return crud.get_grievances_by_user(db, current_user.id)
    if current_user.role == RoleEnum.employee:
        return crud.get_grievances_by_employee(db, current_user.id)
    if current_user.role in (RoleEnum.admin, RoleEnum.super_admin):
        return crud.get_all_grievances(db)
    raise HTTPException(status_code=403, detail="Not authorized")

@router.post("/assign", status_code=status.HTTP_204_NO_CONTENT)
def assign_all(
    db: Session = Depends(get_db),
    current_user: User = Depends(admin_only),
):
    # Only admin and super_admin can assign pending grievances
    crud.assign_grievances_to_employees(db)
    return
