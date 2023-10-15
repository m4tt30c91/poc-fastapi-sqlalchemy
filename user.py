from fastapi import APIRouter

from .service import UserService
from .schema import UserRequest

router = APIRouter(
    prefix="/users",
    tags=["users"]
)

user_service = UserService()

@router.get("/")
async def read_users():
    users = await user_service.read_users()
    return users

@router.post("/")
async def add_user(user_request: UserRequest):
    user = await user_service.add_user(user_request)
    return user