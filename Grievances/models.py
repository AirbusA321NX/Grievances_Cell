from sqlalchemy import Column, Integer, String, ForeignKey
from database import Base

class Grievance(Base):
    __tablename__ = "grievances"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String)
    user_id = Column(Integer, ForeignKey("users.id"))
    department_id = Column(Integer, ForeignKey("departments.id"))
