from sqlalchemy.orm import Session
from . import models, schemas
from User.models import User
from typing import Optional
import uuid

def create_grievance(db: Session, grievance: schemas.GrievanceCreate):
    ticket_id = str(uuid.uuid4())
    db_grievance = models.Grievance(**grievance.dict(), ticket_id=ticket_id)
    db.add(db_grievance)
    db.commit()
    db.refresh(db_grievance)
    return db_grievance

def assign_grievances_to_employees(db: Session):
    grievances = db.query(models.Grievance).filter(models.Grievance.assigned_to == None).all()
    employees = db.query(User).filter(User.role == "employee").all()
    if not employees:
        return
    emp_index = 0
    for i, grievance in enumerate(grievances):
        grievance.assigned_to = employees[emp_index % len(employees)].id
        emp_index += 1
    db.commit()

def get_grievances_by_user(db: Session, user_id: int):
    return db.query(models.Grievance).filter(models.Grievance.user_id == user_id).all()

def get_all_grievances(db: Session):
    return db.query(models.Grievance).all()