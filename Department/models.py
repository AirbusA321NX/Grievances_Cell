from sqlalchemy import Column, Integer, String
from database import Base


class Admin(Base):
    __tablename__ = "Department_detail"

    name = Column(String, index=True)