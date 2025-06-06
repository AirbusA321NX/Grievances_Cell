from fastapi import FastAPI, Request
from pydantic import BaseModel
from starlette.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory="templates")

class Item(BaseModel):
    name: str
    password: str

@app.get("/", response_class=HTMLResponse)
def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "title": "Homepage"})

@app.get("/submit_grievance.html" , response_class=HTMLResponse)
def get_item_by_id(request: Request):
    return templates.TemplateResponse("submit_grievance.html", {"request": request, "title": "Homepage"})

@app.get("/items/")
def list_items():
    return "list"

@app.post("/items/")
async def create_item(item: Item):
    return item
