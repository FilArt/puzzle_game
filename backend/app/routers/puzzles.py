from typing import Annotated

from app.database import get_session
from fastapi import APIRouter, Body, Depends, HTTPException
from sqlmodel import Session

from ..models import Puzzle

router = APIRouter()


@router.get("/puzzle/{puzzle_id}")
def read_puzzle(puzzle_id: int, session: Session = Depends(get_session)):
    puzzle = session.get(Puzzle, puzzle_id)
    if not puzzle:
        raise HTTPException(status_code=404, detail="Item not found")
    return puzzle


@router.post("/check_answer/{puzzle_id}")
def check_answer(
    puzzle_id: int,
    user_answer: Annotated[str, Body()],
    session: Session = Depends(get_session),
):
    puzzle = session.get(Puzzle, puzzle_id)
    if not puzzle:
        raise HTTPException(status_code=404, detail="Item not found")

    if user_answer.lower() == puzzle.answer.lower():
        print(user_answer, puzzle.answer)
        return {"result": "Correct"}
    else:
        return {"result": "Incorrect"}
