
import hashlib
import secrets

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field

router = APIRouter(
    prefix="/api/v1/users",
    tags=["Users"]
)

# Stockage temporaire pour les premiers essais.
users = {}


class UserRegistration(BaseModel):
    username: str = Field(min_length=3, max_length=50)
    email: str = Field(min_length=5, max_length=150)
    password: str = Field(min_length=10, max_length=128)


def hash_password(password: str) -> str:
    salt = secrets.token_bytes(16)

    password_hash = hashlib.scrypt(
        password.encode("utf-8"),
        salt=salt,
        n=2**14,
        r=8,
        p=1
    )

    return (
        salt.hex()
        + ":"
        + password_hash.hex()
    )


@router.post("/register")
def register_user(request: UserRegistration):

    username = request.username.strip()
    email = request.email.strip().lower()

    if not username or not email:
        raise HTTPException(
            status_code=400,
            detail="Username and email are required"
        )

    if "@" not in email or "." not in email:
        raise HTTPException(
            status_code=400,
            detail="Invalid email address"
        )

    if any(
        user["username"].lower() == username.lower()
        for user in users.values()
    ):
        raise HTTPException(
            status_code=409,
            detail="Username already exists"
        )

    if any(
        user["email"] == email
        for user in users.values()
    ):
        raise HTTPException(
            status_code=409,
            detail="Email already exists"
        )

    user_id = len(users) + 1

    user = {
        "id": user_id,
        "username": username,
        "email": email,
        "password_hash": hash_password(request.password),
        "currency": "XOF",
        "status": "SIMULATION"
    }

    users[user_id] = user

    return {
        "id": user_id,
        "username": username,
        "email": email,
        "currency": "XOF",
        "status": "SIMULATION"
    }


@router.get("/")
def list_users():

    return {
        "total": len(users),
        "users": [
            {
                "id": user["id"],
                "username": user["username"],
                "email": user["email"],
                "currency": user["currency"]
            }
            for user in users.values()
        ]
    }
