from fastapi import Depends, APIRouter
from fastapi import FastAPI
from sqlalchemy.orm import Session

from config.database import get_db
from repositories.auth_repo import login_user
from schema.auth import LoginRequest

app = FastAPI()

router = APIRouter(prefix="/auth", tags=["login"])


@router.post("/login")
def user_login(login_data: LoginRequest, db: Session = Depends(get_db)):
    return login_user(db, mail=login_data.mail, password=login_data.password)
