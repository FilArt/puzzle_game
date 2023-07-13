from sqlmodel import Field, SQLModel


class PuzzleList(SQLModel):
    id: int | None = Field(default=None, primary_key=True)


class PuzzleItem(PuzzleList):
    image_urls: str


class Puzzle(PuzzleItem, table=True):
    answer: str
