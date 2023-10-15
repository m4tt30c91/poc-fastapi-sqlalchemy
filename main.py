from fastapi import FastAPI

from .database import async_engine

from .user import router as user_router
from .model import Base

app = FastAPI()
app.include_router(user_router)

@app.on_event("startup")
async def init_database():
    async with async_engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)