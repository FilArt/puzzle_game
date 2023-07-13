from app.database import init_db
from app.routers import puzzles
from app.settings import settings
from fastapi import FastAPI

app = FastAPI()

if settings.DEBUG:
    from fastapi.middleware.cors import CORSMiddleware

    origins = [
        "http://localhost",
        "http://localhost:3000",
    ]

    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )


@app.on_event("startup")
async def on_startup():
    await init_db()


app.include_router(puzzles.router)
