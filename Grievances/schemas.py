from pydantic import BaseModel
from datetime import datetime

class GrievanceCreate(BaseModel):
    grievance: str

class GrievanceUpdate(BaseModel):
    grievance: str | None = None
    status: str | None = None
    assigned_to: int | None = None  

class GrievanceOut(BaseModel):
    id: int
    ticket_id: str
    user_id: int
    department_id: int
    assigned_to: int | None
    status: str
    created_at: datetime

    class Config:
        orm_mode = True
