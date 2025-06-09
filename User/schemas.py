from pydantic import BaseModel, EmailStr

class UserBase(BaseModel):
    email: EmailStr
    department_id: int

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int
    class Config:
        orm_mode = True
