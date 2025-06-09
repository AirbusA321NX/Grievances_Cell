from sqlalchemy.orm import Session
from . import models, schemas
from User.models import User
from roles import RoleEnum
import uuid

def create_grievance(db: Session, grievance: schemas.GrievanceCreate, user_id: int):
    # Generate unique ticket ID
    ticket = str(uuid.uuid4())
    db_g = models.Grievance(
        ticket_id=ticket,
        user_id=user_id,
        department_id=grievance.department_id
    )
    db.add(db_g)
    db.commit()
    db.refresh(db_g)
    return db_g

def assign_grievances_to_employees(db: Session):
    # All unassigned grievances
    pend = db.query(models.Grievance)\
             .filter(models.Grievance.assigned_to.is_(None))\
             .all()
    # All employees
    emps = db.query(User).filter(User.role == RoleEnum.employee).all()
    if not emps:
        return
    # Round-robin assign
    for i, g in enumerate(pend):
        g.assigned_to = emps[i % len(emps)].id
    db.commit()

def get_grievances_by_user(db: Session, user_id: int):
    return db.query(models.Grievance)\
             .filter(models.Grievance.user_id == user_id)\
             .all()

def get_grievances_by_employee(db: Session, employee_id: int):
    return db.query(models.Grievance)\
             .filter(models.Grievance.assigned_to == employee_id)\
             .all()

def get_all_grievances(db: Session):
    return db.query(models.Grievance).all()
