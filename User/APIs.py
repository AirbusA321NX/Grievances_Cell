from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List, Union
from User import crud, schemas, models
from database import get_db
from dependencies import get_current_active_user, RoleChecker
from roles import RoleEnum as Role

router = APIRouter(prefix="/users", tags=["Users"])

role_admin_employee_super = RoleChecker([Role.admin, Role.employee, Role.super_admin])

@router.post("/", response_model=schemas.UserFull)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db),
                current_user: models.User = Depends(role_admin_employee_super)):
    # Only admin or higher can create users
    return crud.create_user(db, user)

@router.get("/", response_model=List[Union[schemas.UserLimited, schemas.UserFull]])
def read_users(db: Session = Depends(get_db),
               current_user: models.User = Depends(get_current_active_user)):
    if current_user.role == Role.user:
        users = crud.get_users(db)
        # Return limited info for normal users
        return [schemas.UserLimited.from_orm(u) for u in users]
    elif current_user.role in [Role.admin, Role.employee, Role.super_admin]:
        users = crud.get_users(db)
        # Return full info for others
        return [schemas.UserFull.from_orm(u) for u in users]
    else:
        raise HTTPException(status_code=403, detail="Not authorized")

@router.get("/{user_id}", response_model=Union[schemas.UserLimited, schemas.UserFull])
def read_user(user_id: int, db: Session = Depends(get_db),
              current_user: models.User = Depends(get_current_active_user)):
    user = crud.get_users(db, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    if current_user.id == user_id or current_user.role in [Role.admin, Role.employee, Role.super_admin]:
        # Return full info for self or admin/employee/super_admin
        return schemas.UserFull.from_orm(user)
    elif current_user.role == Role.user:
        # Normal user sees limited info for others (or restrict fully as per your policy)
        return schemas.UserLimited.from_orm(user)
    else:
        raise HTTPException(status_code=403, detail="Not authorized")
