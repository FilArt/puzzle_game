import pytest
from httpx import AsyncClient

pytestmark = pytest.mark.asyncio


async def test_get_puzzle(client: AsyncClient):
    response = await client.get("/puzzle/1")
    assert response.json()["answer"] == "1"
    assert response.json()["image_urls"] == "1,2,3"


async def test_check_answer_correct(client: AsyncClient):
    response = await client.post("/check_answer/1", json="1")
    result = response.json()
    assert result["result"] == "Correct"


async def test_check_answer_incorrect(client: AsyncClient):
    response = await client.post("/check_answer/1", json="2")
    result = response.json()
    assert result["result"] == "Incorrect"
