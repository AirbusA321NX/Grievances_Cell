from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
import crud, Comments.schemas as schemas
from database import get_db

router = APIRouter(prefix="/comments", tags=["comments"])

@router.post("/", response_model=schemas.Comment)
def create(c: schemas.CommentCreate, db: Session = Depends(get_db)):
    return crud.create_comment(db, c)

@router.get("/grievance/{gid}", response_model=list[schemas.Comment])
def read_by_grievance(gid: int, skip: int=0, limit: int=100, db: Session = Depends(get_db)):
    return crud.get_comments_by_grievance(db, gid, skip, limit)
