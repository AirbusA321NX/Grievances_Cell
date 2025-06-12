# User/schemas.py
from pydantic import BaseModel
from pydantic.networks import EmailStr
from typing import Optional
from roles import RoleEnum

class PasswordReset(BaseModel):
    email: EmailStr
    new_password: str

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
