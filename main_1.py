from typing import Union
from fastapi import FastAPI, Request
from fastapi import FastAPI
from pydantic import BaseModel
from pydantic import BaseModel
from requests import request
from starlette.responses import HTMLResponse
from fastapi.templating import Jinja2Templates


class Item(BaseModel):
    name: str
    password: str

templates = Jinja2Templates(directory="templates")

app = FastAPI()

@app.get("/" , response_class=HTMLResponse )
def read_root():
    return templates.TemplateResponse("index.html", {"request": request, "title": "Homepage"})


@app.get("/items/{item_id}")
def read_item(item_id: int):
    return {"item_id": item_id}


@app.get("/items/")
def read_item():
    return "list"


@app.post("/items/")
async def create_item(item: Item):
    return item