from enum import Enum
from pydantic import BaseModel

class RoleEnum(str, Enum):
    Super_Admin = "Super_Admin"
    Admin = "Admin"
    Employee = "Employee"

class User(BaseModel):
    id: int
    name: str
    email: str
    role: RoleEnum

class UserCreate(User):
    pass

class UserOut(User):
    id: int
