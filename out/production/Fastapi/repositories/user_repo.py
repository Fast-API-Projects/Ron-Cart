from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from db_model.user import User


def get_all_user(db: Session):
    return db.query(User).all()


def create_user(name: str, mail: str, phno: str, hash_password: str, db: Session):
    db_user = User(name=name, mail=mail, phno=phno, password=hash_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def update_user_info(new_mail: str, name: str, phno: str, password: str, db: Session):
    filtered_user = db.query(User).filter(User.mail == new_mail).first()
    if filtered_user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"{new_mail} Not Found")
    filtered_user.name = name
    filtered_user.phno = phno
    filtered_user.password = password
    db.commit()
    db.refresh(filtered_user)
    return filtered_user


def delete_user_info(mail: str, db: Session):
    filtered_user = db.query(User).filter(User.mail == mail).first()
    if filtered_user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"{mail}Mail Not Found")
    db.delete(filtered_user)
    db.commit()
    return "User deleted successfully"
