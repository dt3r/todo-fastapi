from contextlib import asynccontextmanager
from fastapi import FastAPI
from app.orm import create_tables
from app.routers.tasks import router as tasks_router
import uvicorn


@asynccontextmanager
async def lifespan(app: FastAPI):
    create_tables()
    yield

app = FastAPI(lifespan=lifespan)

app.include_router(tasks_router)

@app.get("/")
def get_root():
    return {"status": "running"}


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)