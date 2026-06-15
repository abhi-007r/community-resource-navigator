from passlib.context import CryptContext
from jose import jwt
from datetime import datetime, timedelta
import os
from jose import JWTError
from fastapi import Depends
from fastapi import HTTPException
from fastapi.security import OAuth2PasswordBearer

from dotenv import load_dotenv
oauth2_scheme = OAuth2PasswordBearer(
    tokenUrl="/auth/login"
)

load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM")

pwd_context = CryptContext(
    schemes=["bcrypt"],
    deprecated="auto"
)


def hash_password(password: str):
    return pwd_context.hash(password)


def verify_password(
    plain_password: str,
    hashed_password: str
):
    return pwd_context.verify(
        plain_password,
        hashed_password
    )


def create_access_token(
    data: dict,
    expires_delta: timedelta = timedelta(minutes=30)
):
    to_encode = data.copy()

    expire = datetime.utcnow() + expires_delta

    to_encode.update(
        {
            "exp": expire
        }
    )

    return jwt.encode(
        to_encode,
        SECRET_KEY,
        algorithm=ALGORITHM
    )
def get_current_user(
    token: str = Depends(oauth2_scheme)
):
    try:
        payload = jwt.decode(
            token,
            SECRET_KEY,
            algorithms=[ALGORITHM]
        )

        email = payload.get("sub")

        if email is None:
            raise HTTPException(
                status_code=401,
                detail="Invalid token"
            )

        return email

    except JWTError:
        raise HTTPException(
            status_code=401,
            detail="Invalid token"
        )