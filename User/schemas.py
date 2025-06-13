# User/schemas.py
from pydantic import BaseModel
from pydantic.networks import EmailStr
from typing import Optional
from roles import RoleEnum

class PasswordReset(BaseModel):
    email: EmailStr
    new_password: str

class UserBase(BaseModel):
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
        from_attributes = True

class UserCreate(BaseModel):
    email: str
    password: str
    department_id: Optional[int] = None
    role: RoleEnum
