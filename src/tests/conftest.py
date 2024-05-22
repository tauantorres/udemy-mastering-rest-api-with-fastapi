import os
import pytest

from fastapi.testclient import TestClient
from typing import AsyncGenerator, Generator
from httpx import AsyncClient, ASGITransport


os.environ["ENV_STATE"] = "test"

from src.main import app
from src.database import database

@pytest.fixture(scope="session")
def anyio_backend():
    return "asyncio"

@pytest.fixture()
def client() -> Generator:
    yield TestClient(app)

@pytest.fixture(autouse=True)
async def db() -> AsyncGenerator:
    await database.connect()
    yield
    await database.disconnect()

@pytest.fixture()
async def async_client(client) -> AsyncGenerator:
    async with AsyncClient(transport=ASGITransport(app=app), base_url=client.base_url) as ac:
        yield ac
