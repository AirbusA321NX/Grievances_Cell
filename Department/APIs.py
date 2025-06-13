from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from Department import crud, schemas, models
from database import get_db
from dependencies import get_current_active_user, RoleChecker
from roles import RoleEnum as Role
from User.models import User
from Department.models import Department
from Department.schemas import DepartmentOut, DepartmentCreate
                        

router = APIRouter(prefix="/departments", tags=["Departments"])

role_admin = RoleChecker([Role.admin, Role.super_admin])

@router.post("/", response_model=schemas.DepartmentOut)
def create_department(dept: schemas.DepartmentCreate, db: Session = Depends(get_db),
                          current_user: User = Depends(role_admin)):
    try:
        new_dept = Department(name=dept.name)
        db.add(new_dept)
        db.commit()
        db.refresh(new_dept)
        return new_dept
    except Exception as e:
        print("create_department error:", repr(e))
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/", response_model=List[schemas.Department])
def read_departments(db: Session = Depends(get_db),
                         current_user: User = Depends(get_current_active_user)):
        # Only admin, super_admin, and employees can see departments (users cannot)
        if current_user.role not in [Role.admin.value, Role.employee.value, Role.super_admin.value]:
            raise HTTPException(status_code=403, detail="Not authorized to view departments")
        return crud.get_departments(db)