from fastapi import Depends, FastAPI, APIRouter
from sqlalchemy.orm import Session

from config.database import Base, engine
from config.database import get_db
from config.security import hash_password
from repositories.user_repo import create_user, update_user_info, delete_user_info, get_all_user
from schema.user import UserCreate, User

app = FastAPI()

Base.metadata.create_all(bind=engine)

router = APIRouter(prefix="/user_profile", tags=["user"])


@router.get("/getall")
def get_user(db: Session = Depends(get_db)):
    return get_all_user(db)


@router.post("/signup")
def signup(user: User, db: Session = Depends(get_db)):
    hashed_password = hash_password(user.password)
    return create_user(name=user.name, mail=user.mail, phno=user.phno, hash_password=hashed_password, db=db)


@router.put("/update_user")
def update_user(new_mail: str, user: UserCreate, db: Session = Depends(get_db)):
    return update_user_info(new_mail=new_mail, name=user.name, phno=user.phno, password=user.password,
                            db=db)


@router.delete("/delete_user")
def delete_user(mail: str, db: Session = Depends(get_db)):
    return delete_user_info(mail, db)
