import pytest
import pytest_asyncio
from app.models import Puzzle
from httpx import AsyncClient

pytestmark = pytest.mark.asyncio


@pytest_asyncio.fixture(autouse=True, scope="function")
async def simple_puzzle(session):
    puzzle = Puzzle(id=1, answer="1", image_urls="1,2,3")
    session.add(puzzle)
    await session.commit()
    await session.refresh(puzzle)
    return puzzle


async def test_get_puzzles(client: AsyncClient):
    response = await client.get("/puzzles")
    assert response.json() == [{"id": 1}]


async def test_get_puzzle(client: AsyncClient):
    response = await client.get("/puzzles/1")
    assert response.json() == {"id": 1, "image_urls": "1,2,3"}


async def test_get_puzzle_not_found(client: AsyncClient):
    response = await client.get("/puzzles/2")
    assert response.status_code == 404


async def test_check_answer_correct(client: AsyncClient):
    response = await client.post("/puzzles/1/check_answer", json="1")
    result = response.json()
    assert result is True


async def test_check_answer_incorrect(client: AsyncClient):
    response = await client.post("/puzzles/1/check_answer", json="2")
    result = response.json()
    assert result is False
