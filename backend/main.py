from app.database import create_engine_and_db
from app.routers import puzzles
from fastapi import FastAPI

app = FastAPI()


@app.on_event("startup")
def on_startup():
    create_engine_and_db()


app.include_router(puzzles.router)
