from fastapi import FastAPI, Request
from database import engine, Base
from fastapi.templating import Jinja2Templates

from User.APIs import router as user_router
from Department.APIs import router as dept_router
from Grievances.APIs import router as grievance_router
from Comments.APIs import router as comments_router

Base.metadata.create_all(bind=engine)

app = FastAPI()
templates = Jinja2Templates(directory="templates")

app.include_router(user_router, prefix="/users", tags=["Users"])
app.include_router(dept_router, prefix="/departments", tags=["Departments"])
app.include_router(grievance_router, prefix="/grievances", tags=["Grievances"])
app.include_router(comments_router, prefix="/comments", tags=["Comments"])

@app.get("/")
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})
