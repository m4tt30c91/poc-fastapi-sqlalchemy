from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from .model import User
from .schema import UserResponse, UserRequest
from .database import async_session

class UserService():
    
    async def read_users(self):
        users = []
        async with(async_session()) as session:
            result = await session.execute(select(User))
            for user in result.scalars():
                users.append(UserResponse(id=user.id, name=user.name, surname=user.surname))
        return users
                
    async def add_user(self, user_request: UserRequest):
        async with(async_session()) as session:
            user = User(name=user_request.name, surname=user_request.surname)
            session.add(user)
            await session.commit()
            return UserResponse(id=user.id, name=user.name, surname=user.surname)