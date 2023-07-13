import pytest_asyncio
from app.database import get_session
from httpx import AsyncClient
from main import app
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool
from sqlmodel import Session, SQLModel


@pytest_asyncio.fixture(scope="function", name="session")
async def async_session():
    engine = create_async_engine(
        "sqlite+aiosqlite://",
        connect_args={"check_same_thread": False},
        poolclass=StaticPool,
    )

    session = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)

    async with session() as s:
        async with engine.begin() as conn:
            await conn.run_sync(SQLModel.metadata.create_all)

        yield s

    async with engine.begin() as conn:
        await conn.run_sync(SQLModel.metadata.drop_all)

    await engine.dispose()


@pytest_asyncio.fixture(name="client")
async def client_fixture(session: Session):
    async def get_session_override():
        yield session

    app.dependency_overrides[get_session] = get_session_override
    client = AsyncClient(app=app, base_url="http://localhost:8000")
    yield client
    app.dependency_overrides.clear()
