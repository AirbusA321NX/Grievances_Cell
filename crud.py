from sqlalchemy.orm import Session
from models import User ,Admin , Grievances
from schema import user , UserCreate , Grievances

def get_users(db: Session , User_id : int):
    return (db.query(user).filter(User_id==User.id)).first()

def get_user(db: Session, skip: int = 0, limit: int = 10):
    return db.query(user).offset(skip).limit(limit).all()

def create_user(db: Session, user_data: UserCreate):
    db_user = user(name=user_data.name, email=user_data.email)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def create_grievances(db: Session, content: str , Grievances_id : int , office_department : str , user_name :str):
    db_grievances = Grievances(Grievances_content=content,id=Grievances_id , department=office_department , name=user_name)
    db.add(db_grievances)
    db.commit()
    db.refresh(db_grievances)
    return db_grievances
