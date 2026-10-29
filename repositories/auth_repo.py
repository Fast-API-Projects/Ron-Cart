from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from config.security import verify_password, create_access_token
from db_model.user import User


def login_user(db: Session, mail: str, password: str):
    filtered_password = db.query(User).filter(User.mail == mail).first()
    if filtered_password is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Incorrect Email")
    password_verification = verify_password(password, filtered_password.password)
    if password_verification is False:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Incorrect Password")
    access_token = create_access_token(mail, filtered_password.role)
    return access_token
