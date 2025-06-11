from sqlalchemy.orm import Session
from . import models, schemas
from Department.models import Department
from Department.crud import create_department, get_departments
from passlib.context import CryptContext
from typing import List , Optional

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def create_user(db: Session, user: schemas.UserCreate):
    db_user = models.User(**user.dict())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_users(db: Session, role_filter: List[str] = None):
    query = db.query(models.User)
    if role_filter:
        query = query.filter(models.User.role.in_(role_filter))
    return query.all()

def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()
