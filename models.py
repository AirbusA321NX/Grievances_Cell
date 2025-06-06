from sqlalchemy import Column , Integer , String
from database import Base

class user(Base):
    __tablename__= "user_detail"

    id = Column(Integer ,primary_key = True , index= True)
    name = Column(String , index = True)
    email = Column(String ,Unique = True, index = True)
    password = Column(String , index = True)




    class admin(Base):
        __tablename__ = "admin_detail"

        id = Column(Integer, primary_key=True, index=True)
        name = Column(String, index=True)
        email = Column(String, Unique=True, index=True)
        password = Column(String, index=True)





    class Grievances(Base):
        __tablename__="Grievances"
        name = Column(String , index = True)
        id = Column(Integer , primary_key=True , index = True)
        Grievances_content = Column(String , index = True)
        department = Column(String , index = True)