from pydantic import BaseModel

class GrievanceBase(BaseModel):
    title: str
    description: str
    user_id: int
    department_id: int

class GrievanceCreate(GrievanceBase):
    pass

class Grievance(GrievanceBase):
    id: int

    class Config:
        orm_mode = True
