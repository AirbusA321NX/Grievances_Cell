from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
import crud, database
from Department import models, schemas

router = APIRouter()

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=schemas.Department)
def create_department(dept: schemas.DepartmentCreate, db: Session = Depends(get_db)):
    return crud.create_department(db=db, dept=dept)

@router.get("/", response_model=list[schemas.Department])
def list_departments(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.get_departments(db=db, skip=skip, limit=limit)
