from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from ..utils import helpers

# 👇 Use APIRouter instead of FastAPI here
router = APIRouter()

class GreetRequest(BaseModel):
    name: str

@router.get("/")
def root():
    return {"message": "Greetings API is up and running!"}

@router.post("/")
def greet_user(request: GreetRequest):
    if not request.name.isalpha():
        raise HTTPException(status_code=400, detail="Name must contain only letters.")
    message = helpers.greet(request.name)
    return {"greeting": message}
