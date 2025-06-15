from fastapi import APIRouter

from.schemas import Users
from users import crud


router = APIRouter(prefix="/users", tags=["Users"])


# использовать метод post
@router.post("/")
def create_user(user: Users):
    return crud.create_user(user_in=user)