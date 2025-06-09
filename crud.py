# Grievance_cell/crud.py

from sqlalchemy.orm import Session
from Department.models import Department
from User.models import User
from Grievances.models import Grievance
from Comments.models import Comment
import Department.schemas as dept_s
import User.schemas as user_s
import Grievances.schemas as grv_s
import Comments.schemas as com_s

def create_department(db: Session, department: dept_s.DepartmentCreate):
    db_obj = Department(**department.dict())
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj

def get_departments(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Department).offset(skip).limit(limit).all()

def create_user(db: Session, user: user_s.UserCreate):
    db_obj = User(
        email=user.email,
        password=user.password,
        department_id=user.department_id
    )
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj

def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(User).offset(skip).limit(limit).all()

def create_grievance(db: Session, g: grv_s.GrievanceCreate):
    db_obj = Grievance(
        user_id=g.user_id,
        department_id=g.department_id,
        status=g.status
    )
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj

def get_grievances(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Grievance).offset(skip).limit(limit).all()

def update_grievance_status(db: Session, grievance_id: int, status: str):
    g = db.query(Grievance).filter(Grievance.id == grievance_id).first()
    g.status = status
    db.commit()
    db.refresh(g)
    return g

def create_comment(db: Session, c: com_s.CommentCreate):
    db_obj = Comment(**c.dict())
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj

def get_comments_by_grievance(db: Session, grievance_id: int, skip: int = 0, limit: int = 100):
    return (
        db.query(Comment)
          .filter(Comment.grievance_id == grievance_id)
          .offset(skip)
          .limit(limit)
          .all()
    )
