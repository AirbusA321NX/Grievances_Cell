from datetime import datetime
from pydantic import BaseModel

class Grievances(BaseModel):
    id: int
    department: str
    name: str
    Grievances_content: str
    timestamp: datetime

    class Config:
        orm_mode = True
