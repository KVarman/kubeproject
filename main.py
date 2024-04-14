from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

@app.get("/")
def home():
    return {"Hello": "world"}


class User(BaseModel):
    first_name: str
    last_name : str
    password: str
    phone: int


@app.post("/data")
def data(user_details:User):
    return user_details
