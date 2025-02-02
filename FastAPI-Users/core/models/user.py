from collections.abc import AsyncGenerator

from fastapi import Depends
from fastapi_users.db import SQLAlchemyBaseUserTable, SQLAlchemyUserDatabase
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine
from sqlalchemy.orm import DeclarativeBase

from .base import Base
from .mixins.int_id_pk import IntIdPkMixin


class User(Base, IntIdPkMixin, SQLAlchemyBaseUserTable[int]):
    pass
