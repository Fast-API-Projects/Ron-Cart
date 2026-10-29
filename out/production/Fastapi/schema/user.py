from pydantic import BaseModel, Field


class User(BaseModel):
    name: str
    mail: str
    phno: str
    password: str


class UserCreate(BaseModel):
    name: str
    phno: str
    password: str
