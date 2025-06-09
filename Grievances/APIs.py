from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
import crud, Grievances.schemas as schemas
from database import get_db

router = APIRouter(prefix="/grievances", tags=["grievances"])

@router.post("/", response_model=schemas.Grievance)
def create(g: schemas.GrievanceCreate, db: Session = Depends(get_db)):
    return crud.create_grievance(db, g)

@router.get("/", response_model=list[schemas.Grievance])
def read_all(skip: int=0, limit: int=100, db: Session = Depends(get_db)):
    return crud.get_grievances(db, skip, limit)

@router.patch("/{id}/status", response_model=schemas.Grievance)
def update_status(id: int, status: str, db: Session = Depends(get_db)):
    return crud.update_grievance_status(db, id, status)
