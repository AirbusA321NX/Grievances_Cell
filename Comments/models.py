from sqlalchemy import Column, Integer, String
from database import Base

class Comments(Base):
    __tablename__ = "Comments"

    name = Column(String, index=True)
    comment = Column(String, index=True)