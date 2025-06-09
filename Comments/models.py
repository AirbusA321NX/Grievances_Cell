from sqlalchemy import Column, Integer, String, ForeignKey
from database import Base

class Comment(Base):
    __tablename__ = "comments"
    id = Column(Integer, primary_key=True, index=True)
    content = Column(String, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    grievance_id = Column(Integer, ForeignKey("grievances.id"))
