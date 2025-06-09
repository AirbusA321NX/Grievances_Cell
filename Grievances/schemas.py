from pydantic import BaseModel
from datetime import datetime

class GrievanceCreate(BaseModel):
    department_id: int

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
