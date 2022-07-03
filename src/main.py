from numpy import full
from fastapi import FastAPI
from pydantic import BaseModel
from datetime import date, datetime
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

origins = [
    "*",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Input(BaseModel):
    username: str
    password: str

class User(BaseModel):
    full_name: str
    date_of_birth: str
    email: str
    gender: str
    contact_number: str
    nick_name: str
    last_login: datetime

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/login")
async def login(input: Input):
    print(input)
    if(input and input.username and input.password and input.username == "jornsmith" and input.password == "zWk!8jA9soT" ):
        user = User(
            full_name="Jorn Smith",
            date_of_birth="May 16, 1999",
            email="jornsmith@example.com",
            gender="Male",
            contact_number="1002334757",
            nick_name="Jorn",
            last_login=datetime.now()
        )
        return {
            "status": True,
            "message": "Login Successful",
            "user": user
        }
    
    return {
        "status": False,
        "message": "Invalid Username or Password"
    }
    
