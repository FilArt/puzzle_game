from sqlmodel import Field, SQLModel


class Puzzle(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    image_urls: str
    answer: str

