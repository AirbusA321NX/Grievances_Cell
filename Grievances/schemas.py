from pydantic import BaseModel
from datetime import datetime

class GrievanceBase(BaseModel):
    user_id: int
    department_id: int

class GrievanceCreate(GrievanceBase):
    status: str = "pending"

class Grievance(GrievanceBase):
    id: int
    timestamp: datetime
    status: str
    class Config:
        orm_mode = True
