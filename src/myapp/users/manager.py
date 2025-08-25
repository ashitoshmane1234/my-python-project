from fastapi import Depends
from fastapi_users.db import SQLAlchemyUserDatabase
from fastapi_users import BaseUserManager, UUIDIDMixin
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker
from uuid import UUID
from typing import Any  # <-- ✅ this fixes the NameError

from ..core.database import SQLALCHEMY_DATABASE_URL
from .models import User

DATABASE_URL_ASYNC = SQLALCHEMY_DATABASE_URL.replace("postgresql://", "postgresql+asyncpg://")

async_engine = create_async_engine(DATABASE_URL_ASYNC, future=True, echo=True)
async_session_maker = sessionmaker(async_engine, expire_on_commit=False, class_=AsyncSession)

async def get_user_db(session: AsyncSession = Depends(async_session_maker)):
    yield SQLAlchemyUserDatabase(session, User)

class UserManager(UUIDIDMixin, BaseUserManager[User, UUID]):
    user_db_model = User

    async def on_after_register(self, user: User, request: Any = None):  # ✅ fixed
        print(f"User {user.id} has registered.")

async def get_user_manager(user_db=Depends(get_user_db)):
    yield UserManager(user_db)