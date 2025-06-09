from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from Grievances import crud, schemas, models
from User.models import User
from database import get_db
from dependencies import get_current_active_user, RoleChecker
from roles import RoleEnum as Role
from roles import RoleEnum
from dependencies import RoleChecker

role_admin = RoleChecker([RoleEnum.admin, RoleEnum.super_admin])

router = APIRouter(prefix="/grievances", tags=["Grievances"])

role_user = RoleChecker([Role.user, Role.employee, Role.admin, Role.super_admin])

@router.post("/", response_model=schemas.Grievance)
def create_grievance(grievance: schemas.GrievanceCreate, db: Session = Depends(get_db),
                     current_user: User = Depends(get_current_active_user)):
    # User creates grievance
    if current_user.role != Role.user.value:
        raise HTTPException(status_code=403, detail="Only users can raise grievances")
    grievance.user_id = current_user.id
    grievance.status = "pending"
    grievance.assigned_to = None
    return crud.create_grievance(db, grievance)

@router.get("/", response_model=List[schemas.Grievance])
def read_grievances(db: Session = Depends(get_db), current_user: User = Depends(get_current_active_user)):
    # Users see only their grievances
    # Employees see grievances assigned to them
    # Admins and super_admins see all grievances
    if current_user.role == Role.user.value:
        return crud.get_grievances_by_user(db, current_user.id)
    elif current_user.role == Role.employee.value:
        return db.query(models.Grievance).filter(models.Grievance.assigned_to == current_user.id).all()
    elif current_user.role in [Role.admin.value, Role.super_admin.value]:
        return crud.get_all_grievances(db)
    else:
        raise HTTPException(status_code=403, detail="Not authorized")

@router.post("/assign", status_code=status.HTTP_204_NO_CONTENT)
def assign_grievances(db: Session = Depends(get_db), current_user: User = Depends(role_admin)):
    # Only admin and super_admin can assign grievances to employees
    crud.assign_grievances_to_employees(db)
    return

@router.post("/assign", status_code=204)
def assign_grievances(db: Session = Depends(get_db), current_user: models.User = Depends(role_admin)):
    # Admin or super admin only
    crud.assign_grievances_to_employees(db)
    return
