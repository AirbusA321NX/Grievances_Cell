# User/schemas.py
from pydantic import BaseModel
from typing import Optional
from roles import RoleEnum

class UserBase(BaseModel):
    user_id: Optional[int] = None
    email: str
    password: str
    department_id: Optional[int] = None
    role: RoleEnum = RoleEnum.user

class UserLimited(UserBase):
    # no department info here
    pass

class UserFull(UserBase):
    department_id: Optional[int]

    class Config:
        orm_mode = True

class UserCreate(BaseModel):
    user_id: Optional[int] = None
    email: str
    password: str
    department_id: Optional[int] = None
    role: RoleEnum
