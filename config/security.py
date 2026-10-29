from datetime import datetime, timezone, timedelta

import jwt
from pwdlib import PasswordHash

from config.config import settings

password_hash = PasswordHash.recommended()


def hash_password(password: str):
    return password_hash.hash(password)


def verify_password(plain_password: str, hashed_password: str):
    return password_hash.verify(plain_password, hashed_password)


# header=algorithm
# payload=user_id,Role,expiry

def create_access_token(user_email: str, role: str):
    expiry = datetime.now(timezone.utc) + timedelta(minutes=settings.JWT_ACCESS_TOKEN_EXPIRY)
    payload = {"sub": user_email,
               "role": role,
               "exp": expiry
               }
    token = jwt.encode(payload, settings.JWT_SECRET_KEY, algorithm=settings.JWT_ALGORITHM)
    return token
