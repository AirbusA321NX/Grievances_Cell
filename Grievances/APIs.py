from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
import crud, database
from Grievances import models, schemas

router = APIRouter()

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=schemas.Grievance)
def create_grievance(gr: schemas.GrievanceCreate, db: Session = Depends(get_db)):
    return crud.create_grievance(db=db, grievance=gr)

@router.get("/", response_model=list[schemas.Grievance])
def list_grievances(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.get_grievances(db=db, skip=skip, limit=limit)
