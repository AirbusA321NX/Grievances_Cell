from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from dependencies import get_db, get_current_user, require_role
from roles import RoleEnum
from User import schemas, crud

router = APIRouter(prefix="/users", tags=["Users"])

@router.get("/me", response_model=schemas.UserOut)
def get_my_info(current_user=Depends(get_current_user)):
    return current_user

@router.get("/all", response_model=list[schemas.UserOut])
def list_users(db: Session = Depends(get_db),
               current_user=Depends(require_role([RoleEnum.admin, RoleEnum.super_admin]))):
    return crud.get_users(db, role_filter=["user", "employee"])  # Only basic roles visible
