from sqlalchemy.orm import Session
from . import models, schemas
from typing import List

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
