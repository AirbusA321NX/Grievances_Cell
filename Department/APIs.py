from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
import crud, Department.schemas as schemas
from database import get_db

router = APIRouter(prefix="/departments", tags=["departments"])

@router.post("/", response_model=schemas.Department)
def create(dept: schemas.DepartmentCreate, db: Session = Depends(get_db)):
    return crud.create_department(db, dept)

@router.get("/", response_model=list[schemas.Department])
def read_all(skip: int=0, limit: int=100, db: Session = Depends(get_db)):
    return crud.get_departments(db, skip, limit)
