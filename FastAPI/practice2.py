from fastapi import FastAPI, status
from datetime import datetime
from pydantic import BaseModel

app = FastAPI()

# this is our pydantic model which stores and structures the data according to format of datata which is provided in base model 
class user(BaseModel):
    name: str
    age: int 
    password: str

# this is a response model which is been send or responded to frontend of our application
# basic pourpose of this reponse model is to hide the complicated or secret data like {passwords, keys, tokens} etc
# this models are used for hiding data from users 
class userResponse(BaseModel):
    name: str
    age: int 

# this is a classsic fuction defined underneath wherre the complicated/sensitive data is keppt hidde using respose models where passwords id been passed 
# but user is unable to see in response window
# hence here output is formatted
@app.get("/user", response_model=userResponse)
def get_user():
    return {"name": "jai", "age": 23, "password": "imortalJKS!1"}

# status code and responses

