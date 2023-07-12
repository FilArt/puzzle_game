import pytest
from app.models import Puzzle
from fastapi.testclient import TestClient
from sqlmodel import Session


@pytest.fixture(scope="function", autouse=True)
def simple_puzzle(session: Session):
    puzzle = Puzzle(id=1, answer="1", image_urls="1,2,3")
    session.add(puzzle)
    session.commit()
    session.refresh(puzzle)
    return puzzle


def test_get_puzzle(client):
    response = client.get("/puzzle/1")
    assert response.json()["answer"] == "1"
    assert response.json()["image_urls"] == "1,2,3"


def test_check_answer_correct(client: TestClient):
    response = client.post("/check_answer/1", json="1")
    result = response.json()
    assert result["result"] == "Correct"


def test_check_answer_incorrect(client):
    response = client.post("/check_answer/1", json="2")
    result = response.json()
    assert result["result"] == "Incorrect"
