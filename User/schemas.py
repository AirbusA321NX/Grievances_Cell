# User/schemas.py
from pydantic import BaseModel
from roles import RoleEnum

class UserBase(BaseModel):
    email: str
    role: RoleEnum

class UserCreate(UserBase):
    password: str
    department_id: int | None = None

class UserOut(UserBase):
    id: int

    class Config:
        orm_mode = True
