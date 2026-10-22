from contextlib import asynccontextmanager
from fastapi import FastAPI, Path, Body, status, Depends
from fastapi.responses import JSONResponse
from typing import Annotated
from pydantic import BaseModel
from database import session_factory
from orm import create_tables
from models.models import Task
from sqlalchemy.exc import OperationalError
from sqlalchemy.orm import Session
import uvicorn
import sys

@asynccontextmanager
async def lifespan(app: FastAPI):
    print("creating tables")
    try:
        create_tables()
        print("Successfuly created tables.")
    except OperationalError as e:
        print(f"Failed to create tables. Details: {e}")
        sys.exit()
    yield
    print("shutting down")

def get_session():
    with session_factory() as session:
        yield session

SessionDep = Annotated[Session, Depends(get_session)]

app = FastAPI(lifespan=lifespan)

class TaskUpdate(BaseModel):
    name: str | None = None
    finished: bool | None = None

tasks = []

next_task_id = 1


@app.get("/")
def get_root():
    return {"status": "running"}

@app.get("/tasks/")
def get_tasks(session: SessionDep):
    return session.query(Task).all()

"""
@app.post("/tasks/", status_code=status.HTTP_201_CREATED)
def post_tasks(task: Task):
    global next_task_id
    new_task = {"id": next_task_id, 
                **task.model_dump()}
    
    tasks.append(new_task)
    next_task_id += 1
    return new_task

"""

"""
@app.get("/tasks/{id}")
def get_task(id: Annotated[int, Path(gt=0)]):
    for task in tasks:
        if task["id"] == id:
            return task
        
    return JSONResponse(status_code=status.HTTP_404_NOT_FOUND,
                        content={"message": "task does not exist"})
"""

"""
@app.patch("/tasks/{id}")
def patch_task(id: Annotated[int, Path(gt=0)], data: TaskUpdate):
    for task in tasks:
        if task["id"] == id:
            task.update(data.model_dump(exclude_unset=True))
            return task

    return JSONResponse(
        status_code=404,
        detail="Task does not exist"
    )
"""
    
"""
@app.delete("/tasks/{id}")
def delete_task(id: int):
    for task in tasks:
        if task["id"] == id:
            tasks.remove(task)
            return {"message": "task deleted", "task": id}

    return JSONResponse(status_code=status.HTTP_404_NOT_FOUND,
                                 content={"message": "task does not exist"})
"""

if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)