from pydantic import BaseModel, Field


class LoginRequest(BaseModel):
    mail: str
    password: str
