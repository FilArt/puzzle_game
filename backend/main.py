from app.database import init_db
from app.routers import puzzles
from fastapi import FastAPI

app = FastAPI()


@app.on_event("startup")
async def on_startup():
    await init_db()


app.include_router(puzzles.router)
