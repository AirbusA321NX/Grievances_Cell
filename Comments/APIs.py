from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
import crud, database
from Comments import models, schemas

router = APIRouter()

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=schemas.Comment)
def create_comment(comment: schemas.CommentCreate, db: Session = Depends(get_db)):
    return crud.create_comment(db=db, comment=comment)

@router.get("/", response_model=list[schemas.Comment])
def list_comments(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.get_comments(db=db, skip=skip, limit=limit)
