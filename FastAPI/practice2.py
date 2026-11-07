from fastapi import FastAPI, HTTPException, status
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

# here we are using status code to show the status of our request and response
@app.post("/create_user", status_code=status.HTTP_201_CREATED)
def create_user():
    return {"message": "user created successfully"}

# here we are using status code to show the status of our request and response
# as we are using path parameter here so we are checking if user_id is not equal to 1 then we are raising an exception with status code 404 
# and detail message "User not found"
@app.get("/user/{user_id}")
def get_user(user_id: int):
    if user_id != 1:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    return {"name": "jai", "age": 23, "password": "imortalJKS!1"}

# Exception Handling
# ovver here we are using try and except block to handle the exception which is raised in get_user function
# where we are checking if user_id is not equal to 1 then we are raising an exception with status code 404 
# and detail message "User not found" and we are catching that exception in except block and returning the error message and 
# status code in response
@app.get("/user/{user_id}")
def user_exception_handling(user_id: int):
    try:
        if user_id != 1:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
        return {"name": "jai", "age": 23, "password": "imortalJKS!1"}
    except HTTPException as e:
        return {"error": e.detail, "status_code": e.status_code}
    except Exception as e:
        return {"error": str(e), "status_code": status.HTTP_500_INTERNAL_SERVER_ERROR}

class userNotFoundException(Exception):
    def __init__(self, name: str):
        self.name = name

@app.get("/user/{name}")
def get_user_by_name(name: str):
    if name != "jai":
        raise userNotFoundException(name)
    return {"name": "jai", "age": 23, "password": "imortalJKS!1"}
