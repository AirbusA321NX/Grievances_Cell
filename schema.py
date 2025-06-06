from pydantic import BaseModel

class user(BaseModel):
    id : int
    name : str
    email :str


class UserCreate(user):
    pass

class UserOut(user):
    id: int

class Grievances(BaseModel):
    id : int
    department : str
    name : str
    Grievances_content  : str


#for let pydantic work with orm based database

    class Config:
        orm_mode = True