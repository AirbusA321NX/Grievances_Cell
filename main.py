from fastapi import FastAPI
from database import engine, Base
from Department.APIs import router as dept_router
from User.APIs import router as user_router
from Grievances.APIs import router as grv_router
from Comments.APIs import router as com_router
import User.APIs as user_apis
import auth

Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(dept_router)
app.include_router(user_router)
app.include_router(user_apis.router)
app.include_router(auth.router)
app.include_router(grv_router)
app.include_router(com_router)
