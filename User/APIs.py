from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List, Union

from User import crud, schemas, models
from database import get_db
from dependencies import get_current_active_user, RoleChecker
from roles import RoleEnum as Role

router = APIRouter(prefix="/users", tags=["Users"])

# Only admin, employee, super_admin can create users
role_admin_employee_super = RoleChecker([Role.admin, Role.employee, Role.super_admin])

@router.post("/", response_model=schemas.UserFull)
def create_user(
    user: schemas.UserCreate,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(role_admin_employee_super),
):
    return crud.create_user(db, user)


@router.get("/", response_model=List[Union[schemas.UserLimited, schemas.UserFull]])
def read_users(
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_active_user),
):
    users = crud.get_users(db)
    if current_user.role == Role.user:
        # Normal users see limited info only
        return [schemas.UserLimited.from_orm(u) for u in users]
    # Admin/Employee/Super see full info
    return [schemas.UserFull.from_orm(u) for u in users]


@router.get("/{user_id}", response_model=Union[schemas.UserLimited, schemas.UserFull])
def read_user(
    user_id: int,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_active_user),
):
    # Fetch a single user by ID
    user = crud.get_user(db, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    # Self or elevated roles see full info
    if current_user.id == user_id or current_user.role in [Role.admin, Role.employee, Role.super_admin]:
        return schemas.UserFull.from_orm(user)

    # Other normal users see limited info
    if current_user.role == Role.user:
        return schemas.UserLimited.from_orm(user)

    raise HTTPException(status_code=403, detail="Not authorized")
