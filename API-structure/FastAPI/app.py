from fastapi import FastAPI
from pydantic import BaseModel 

api = FastAPI() #http://127.0.0.1:8000/docs

class MyItem(BaseModel):
    name: str 
    price: float
    ready: int

@api.get("/")
async def home():
    return "This is home"

@api.post("/submit")
async def submit(item:MyItem):
    return item