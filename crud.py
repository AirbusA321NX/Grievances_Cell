from sqlalchemy.orm import Session
from Comments import models as comment_models, schemas as comment_schemas
from Department import models as dept_models, schemas as dept_schemas
from Grievances import models as grievance_models, schemas as grievance_schemas
from User import models as user_models, schemas as user_schemas


def get_user(db: Session, user_id: int):
    return db.query(user_models.User).filter(user_models.User.id == user_id).first()

def get_users(db: Session, skip: int = 0, limit: int = 10):
    return db.query(user_models.User).offset(skip).limit(limit).all()

def create_user(db: Session, user: user_schemas.UserCreate):
    db_user = user_models.User(name=user.name, email=user.email)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

# --- Department CRUD ---
def get_department(db: Session, dept_id: int):
    return db.query(dept_models.Department).filter(dept_models.Department.id == dept_id).first()

def get_departments(db: Session, skip: int = 0, limit: int = 10):
    return db.query(dept_models.Department).offset(skip).limit(limit).all()

def create_department(db: Session, dept: dept_schemas.DepartmentCreate):
    db_dept = dept_models.Department(name=dept.name)
    db.add(db_dept)
    db.commit()
    db.refresh(db_dept)
    return db_dept

# --- Grievance CRUD ---
def get_grievance(db: Session, grievance_id: int):
    return db.query(grievance_models.Grievance).filter(grievance_models.Grievance.id == grievance_id).first()

def get_grievances(db: Session, skip: int = 0, limit: int = 10):
    return db.query(grievance_models.Grievance).offset(skip).limit(limit).all()

def create_grievance(db: Session, grievance: grievance_schemas.GrievanceCreate):
    db_gr = grievance_models.Grievance(
        title=grievance.title,
        description=grievance.description,
        user_id=grievance.user_id,
        department_id=grievance.department_id
    )
    db.add(db_gr)
    db.commit()
    db.refresh(db_gr)
    return db_gr

# --- Comment CRUD ---
def get_comment(db: Session, comment_id: int):
    return db.query(comment_models.Comment).filter(comment_models.Comment.id == comment_id).first()

def get_comments(db: Session, skip: int = 0, limit: int = 10):
    return db.query(comment_models.Comment).offset(skip).limit(limit).all()

def create_comment(db: Session, comment: comment_schemas.CommentCreate):
    db_cm = comment_models.Comment(
        content=comment.content,
        user_id=comment.user_id,
        grievance_id=comment.grievance_id
    )
    db.add(db_cm)
    db.commit()
    db.refresh(db_cm)
    return db_cm
