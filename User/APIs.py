from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
import crud, User.schemas as schemas
from database import get_db

router = APIRouter(prefix="/users", tags=["users"])

@router.post("/", response_model=schemas.User)
def create(user: schemas.UserCreate, db: Session = Depends(get_db)):
    return crud.create_user(db, user)

@router.get("/", response_model=list[schemas.User])
def read_all(skip: int=0, limit: int=100, db: Session = Depends(get_db)):
    return crud.get_users(db, skip, limit)
