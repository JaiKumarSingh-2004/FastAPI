
from fastapi import FastAPI
from datetime import datetime
from pydantic import BaseModel

app = FastAPI()

# this is field path of this file in my local machine and this is used to run the FastAPI application in the virtual environment.
# C:\Users\jaiku\Downloads\FastAPI-20261019T180749Z-1-001\FastAPI\practice.py

# here we are using type hinting to specify the types of the parameters and return type of the function 
# and also we are using title() method to capitalize the first letter of the first name and last name 
# and also we are using str() method to convert the age to string and then concatenating all the strings to get the full name.

# def get_full_name(first_name: str, last_name: str, age: int):
#     full_name = first_name.title() + " " + last_name.title()+ " " + str(age)
#     return full_name


# print(get_full_name("john", "doe", 32))

#here we are using type hinting to specify the types of the parameters and return type of the function

# def process_items(items: list[str | int]) -> list[str | int]:
#     for item in items:
#         print(item)

# print (process_items({1,2,3,4,5,6,7,8,9,0}))


# this address below is used to activate the virtual environment in windows and then we can run the FastAPI application in the virtual environment. 
# C:\Users\jaiku\Downloads\FastAPI-20261019T180749Z-1-001\FastAPI\env\Scripts\activate.bat

# this address below is used to deactivate virtual environment in windows and then we can run the FastAPI application in the virtual environment.
# C:\Users\jaiku\Downloads\FastAPI-20261019T180749Z-1-001\FastAPI\env\Scripts\deactivate.bat

# this is a pydantic model which is used to validate the data and 
# also to convert the data to the required type and also to provide default values for the fields.
# and it also extends the BaseModel class which is provided by pydantic library.
# it type casts the data to the required type and also provides default values for the fields which are defined in our pydantic model.
class PydanticModel(BaseModel):
    id: int
    name: str
    salary: float
    signup_ts: datetime | None = None

dictionary = {"id": "123", "name": "Jai_Kumar_Singh", "salary": "32000.00", "signup_ts": "2017-06-01 12:22"}

result = PydanticModel(**dictionary)

# print(result)
# print(result.id)

# here we are starting the FastAPI application and defining the routes and their corresponding functions.
@app.get("/")
def read_root():
    return {"message": "welcome to my soul society!"}

# this is our home page where we are returning the data of the Pydantic model in the response 
# and also we are using the result variable which is an instance of the Pydantic model 
# and we are returning the data of the Pydantic model in the response.
# home page
@app.get("/home")
def home():
    return {
        "id": result.id,
        "name": result.name,
        "salary": result.salary,
        "signup_ts": result.signup_ts
    }

#about page
@app.get("/about")
def about():
    return {"message": "This is about page of FastAPI"}

#user page
# here we are using path parameter to get the user id from the url and return the user id in the response and validation
# is done by using the type hinting of the parameter and if the user id is not an integer then it will return a 422 error 
# and if the user id is an integer then it will return the user id in the response.
# here u have to provide user id in the url like this /users/1 and it will return the user id in the response.
@app.get("/users/{user_id}")
def getuser(user_id: int): 
    return {"user_id": user_id, "message": "This is user page of FastAPI"}

# here we are using query parameter to get the user name from the url and return the user name in the response and validation
# is done by using the type hinting of the parameter and if the user name is not a string then it will return a 422 error and 
# if the user name is a string then it will return the user name in the response.
# and we are also using default value for the parameter and if the user name is not provided in the url then it will return the default value.
# here u have to provide user name in the url like this /username?name=Jai_Kumar_Singh and it will return the user name in the response.
# this is optional parameter and if the user name is not provided in the url then it will return the default value.
@app.get("/username")
def get_username(name: str | None = None):
    return {"message": f"Hello, {name}! This is about page of FastAPI"}

# here we are using query parameter to get the limit from the url and return the limit in the response and validation
# is done by using the type hinting of the parameter and if the limit is not an integer then it will return a 422 error and 
# if the limit is an integer then it will return the limit in the response.
@app.get("/products")
def get_products(limit: int = 2000):
    return {"Limit": limit}

# herer we are handling multiple query parameters in the url and also we are using default values for the parameters 
# and if the parameters are not provided in the url then it will return the default values.
# to provide data for multiple query parameters in the url like this /items?name=Jai_Kumar_Singh&prn=123456 and 
# it will return the data in the response.
@app.get("/items")
def get_items(name: str = None, prn: int = 0):
    return {"name": name, "prn": prn}

#here we are using post method to create a student and also we are using request body to get the student data from the request 
# and return the student data in the response.
# where student is a dictionary which contains the student data and we are using default value for the student parameter
# student data is passed in the request body in json format 
# and if the student data is not provided in the request body then 
# it will return the default value which is an empty dictionary.
@app.post("/create_student")
def create_student(student: dict = {}):
    return {"message": "Student created successfully", "student": student}

# here this is a pydantic model which is used to validate the data and also to convert the data to the required type 
# and also to provide default values for the fields.
# and it also extends the BaseModel class which is provided by pydantic library.
# and we are using this pydantic model to validate the data which is passed in the request body in json format
# and if the data is not valid then it will return a 422 error and if the data is valid then it will return the data in the response.
class employee(BaseModel):
    id: int
    name: str
    age: int
    email: str
    salary: float

# here we are using post method to create an employee and also we are using request body to get the employee data from the request
# and return the employee data in the response.
# here data is passed in the request body in json format and if the employee data is not provided in the request body then
# it will return the default value which is an empty dictionary.
# here we are using pydantic model to validate the data 
# and also to convert the data to the required type and also to provide default values for the fields which are defined in our pydantic model 
# which extends Base class.
@app.post("/create_employee")
def create_employee(emp: employee):
    return {"message": "Employee created successfully", "employee": emp}    

# here we are designing a nested pydantic model which is used to validate the data and also to convert the data to the required type
# and also to provide default values for the fields which are defined in our pydantic model
class Address(BaseModel):
    street: str
    city: str
    state: str
    zip_code: int

# here we are designing a nested pydantic model which is used to validate the data and also to convert the data to the required type
# and also to provide default values for the fields which are defined in our pydantic model
# and here we have nested the Address model inside the employee_with_address model which is used to validate the data 
# and also to convert the data to the required type
class employee_with_address(employee):
    name: str
    age: int
    address: Address

# this is a post method which is used to get the employee data from the request body in json format and return the employee data in the response.
# where data is passed in the request body in json format and if the employee data is not provided in the request body then
# it will return the default value which is an empty dictionary.
# also over here we have implemented the nested pydantic model which is used to validate the data 
# and also to convert the data to the required type
@app.post("/get_employee")
def get_employee(emp: employee_with_address):
    return {"message": "Employee data retrieved successfully", "employee": emp}

# here we will create a todo API for practice and we will use pydantic model to validate the data 
# and also to convert the data to the required type
class Todo(BaseModel):
    id: int
    title: str
    description: str | None = None
    completed: bool = False

# here we will create a list to store the todos and we will use this list to store the todos which are created by the user
todos = []

# here we will create a post method which is used to create a todo and also we are using request body to get the todo data from the request
# and return the todo data in the response.
# here data is passed in the request body in json format and if the todo data is not provided in the request body then
# it will return the default value which is an empty list todos.
# it appends the todo data to the todos list and return the message and the todo data in the response.
@app.post("/todos")
def create_todo(todo: Todo):
    todos.append(todo)
    return {"message": "Todo created successfully", "todo": todo}

# here we will create a get method which is used to get the todos and return the todos in the response.
# means that it will return the list of todos which are created by the user and stored in the todos list.
@app.get("/todos")
def get_todos():
    return {"todos": todos}

# here we will create a get method which is used to get the todo by id and return the todo in the response.
# basically it will return the todo which is created by the user 
# and stored in the todos list by matching the id of the todo with the id provided in the url.
# like this /todos/1 and it will return the todo with id 1 in the response.
@app.get("/todos/{todo_id}")
def get_todo(todo_id: int):
    if todo_id < 0 or todo_id >= len(todos):
        return {"message": "Todo not found"}
    for i in range(len(todos)):
        if todos[i].id == todo_id:
            return {"todo": todos[i]}
    return {"message": "ID not found"}

# here we will create a put method which is used to update the todo by id and return the updated todo in the response.
# basically it will update the todo which is created by the user and stored in the todos list
# here we are updatind a specific id todo with new todo data which is passed in the request body in json format 
# and if the todo data is not provided in the request body then it will return the default value which is an empty list todos.
@app.put("/todos/{todo_id}")
def update_todo(todo_id: int, updated_todo: Todo):
    for index, todo in enumerate(todos):
        if todo.id == todo_id:
            todos[index] = updated_todo
            return {"message": "Todo updated successfully", "todo": updated_todo} 
    return {"message": "Todo not found"}

# here we will create a delete method which is used to delete the todo by id and return the message in the response.
# basically it will delete the todo which is created by the user and stored in the todos list
@app.delete("/todos/{todo_id}")
def delete_todo(todo_id: int):
    for index, todo in enumerate(todos):
        if todo.id == todo_id:
            todos.pop(index)
            return {"message": "Todo deleted successfully"}
    return {"message": "Todo not found"}

# here we have created a list on local storage where all the response of runtime API is been stored after been validated and structured using Pydantic models
user_data = []

# this is our pydantic model implemented on this class where it helps us to validate and type cast user data accordingly and help to structure them accordingly
class User(BaseModel):
    id: int
    name: str
    email: str

# this is our post request where all the response data for each user is been appended to the list declared above as user_data
@app.post("/user")
def create_user(user: User):
    user_data.append(user)
    return {"message": "User created successfully", "user": user}

# path+Query+body combo
# put /users/101?nitify=true
# here this put methord is bbeen declared where this methord role is to implement path and query parameter together 
# where path for any user id has been passed and we have set a flag named notigy which must be true to update data and 
# is is passed to api as a query parameter.
@app.put("/users/{user_id}")
def update_user(user_id: int, notify: bool = False, user: User = None):
    if user_id < 0 or user_id >= len(user_data):
        return {"message": "User not found"}
    return {
        "message": "User updated successfully",
        "user_id": user_id,
        "notify": notify,
        "user": user
    }
