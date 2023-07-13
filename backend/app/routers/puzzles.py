from typing import Annotated

from app.database import AsyncSession, get_session
from fastapi import APIRouter, Body, Depends, HTTPException
from sqlmodel import select

from ..models import Puzzle, PuzzleItem, PuzzleList

router = APIRouter()


@router.get("/puzzles", response_model=list[PuzzleList])
async def read_puzzles(
    session: Annotated[AsyncSession, Depends(get_session)]
) -> list[PuzzleList]:
    results = await session.execute(select(Puzzle))
    return results.scalars().all()


@router.get("/puzzles/{puzzle_id}", response_model=PuzzleItem)
async def read_puzzle(
    puzzle_id: int, session: Annotated[AsyncSession, Depends(get_session)]
) -> PuzzleItem:
    puzzle = await session.get(Puzzle, puzzle_id)
    if not puzzle:
        raise HTTPException(status_code=404, detail="Item not found")
    return puzzle


@router.post("/puzzles/{puzzle_id}/check_answer")
async def check_answer(
    puzzle_id: int,
    user_answer: Annotated[str, Body()],
    session: Annotated[AsyncSession, Depends(get_session)],
) -> bool:
    puzzle = await session.get(Puzzle, puzzle_id)
    if not puzzle:
        raise HTTPException(status_code=404, detail="Item not found")
    return user_answer.lower() == puzzle.answer.lower()
