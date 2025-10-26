import contextlib

from sqlalchemy import MetaData
from sqlalchemy.orm import declarative_base
from sqlalchemy.ext.asyncio import (
    create_async_engine,
    AsyncConnection,
    AsyncSession,
    async_sessionmaker,
)
from typing import AsyncIterator
from core import settings

metadata = MetaData()
Base = declarative_base(metadata=metadata)


class DatabaseSessionManager:
    def __init__(self, database_url: str):
        self._engine = create_async_engine(database_url, echo=settings.is_development)
        self._sessionmaker = async_sessionmaker(
            bind=self._engine, expire_on_commit=False
        )

    async def close(self) -> None:
        if self._engine is None:
            raise Exception("DatabaseSessionManager is not initialized")

        await self._engine.dispose()

        self._engine = None
        self.SessionLocal = None

    @contextlib.asynccontextmanager
    async def connect(self) -> AsyncIterator[AsyncConnection]:
        if self._engine is None:
            raise Exception("DatabaseSessionManager is not initialized")

        async with self._engine.begin() as connection:
            try:
                yield connection
            except Exception:
                await connection.rollback()
                raise

    @contextlib.asynccontextmanager
    async def session(self) -> AsyncIterator[AsyncSession]:
        if self._sessionmaker is None:
            raise Exception("DatabaseSessionManager is not initialized")

        async with self._sessionmaker() as session:
            try:
                yield session
            except Exception:
                await session.rollback()
                raise


session_manager = DatabaseSessionManager(settings.database_url)


async def get_db_session() -> AsyncIterator[AsyncSession]:
    async with session_manager.session() as session:
        yield session
