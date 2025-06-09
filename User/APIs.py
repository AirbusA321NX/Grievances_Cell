from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
import crud, database
from User import models, schemas

router = APIRouter()

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    return crud.create_user(db=db, user=user)

@router.get("/", response_model=list[schemas.User])
def list_users(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.get_users(db=db, skip=skip, limit=limit)
