from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from User import crud, schemas, models
from database import get_db
from dependencies import get_current_active_user, RoleChecker
from roles import RoleEnum as Role

router = APIRouter(prefix="/users", tags=["Users"])

role_user = RoleChecker([Role.admin, Role.employee, Role.super_admin])

@router.post("/", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db),
                current_user: models.User = Depends(role_user)):
    # Only admin or higher can create users
    return crud.create_user(db, user)

@router.get("/", response_model=List[schemas.User])
def read_users(db: Session = Depends(get_db),
               current_user: models.User = Depends(role_user)):
    # Admin, employee, super_admin can view users
    allowed_roles = [Role.admin.value, Role.employee.value, Role.super_admin.value]
    if current_user.role not in allowed_roles:
        raise HTTPException(status_code=403, detail="Not authorized")
    # Employees cannot see departments or roles details (enforced in frontend or filtering)
    return crud.get_users(db)

@router.get("/{user_id}", response_model=schemas.User)
def read_user(user_id: int, db: Session = Depends(get_db),
              current_user: models.User = Depends(get_current_active_user)):
    # User can see only their own info, or admin/employee/super admin can see any user
    if current_user.id != user_id and current_user.role not in [Role.admin.value, Role.employee.value, Role.super_admin.value]:
        raise HTTPException(status_code=403, detail="Not authorized")
    user = crud.get_user(db, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user
