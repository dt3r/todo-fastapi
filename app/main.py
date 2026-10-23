from contextlib import asynccontextmanager
from fastapi import FastAPI, Path, Body, status, Depends, HTTPException, Response
from typing import Annotated
from pydantic import BaseModel
from database import session_factory
from orm import create_tables
from models.models import Task
from sqlalchemy.orm import Session
import uvicorn


@asynccontextmanager
async def lifespan(app: FastAPI):
    create_tables()
    yield

def get_session():
    with session_factory() as session:
        yield session

SessionDep = Annotated[Session, Depends(get_session)]

app = FastAPI(lifespan=lifespan)

class TaskCreate(BaseModel):
    task_name: str
    finished: bool = False 

class TaskUpdate(BaseModel):
    task_name: str | None = None
    finished: bool | None = None

class TaskResponse(BaseModel):
    id: int
    name: str
    finished: bool


@app.get("/")
def get_root():
    return {"status": "running"}

@app.get("/tasks/")
def get_tasks(session: SessionDep):
    tasks = session.query(Task).all()

    return [
        TaskResponse(
            id=task.id,
            name=task.task_name,
            finished=task.finished
        ) for task in tasks
    ]
                        

@app.post("/tasks/", status_code=status.HTTP_201_CREATED)
def post_tasks(task_data: TaskCreate, session: SessionDep):
    task = Task(**task_data.model_dump())

    session.add(task)
    session.commit()
    session.refresh(task)

    return TaskResponse(
        id=task.id,
        name=task.task_name,
        finished=task.finished
    )

    
@app.get("/tasks/{id}")
def get_task(id: Annotated[int, Path(gt=0)], session: SessionDep):
    task = session.get(Task, id)

    if task is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail={"message": "task does not exist"}
        )

    return TaskResponse(
        id=task.id,
        name=task.task_name,
        finished=task.finished,
    )



@app.patch("/tasks/{id}")
def patch_task(id: Annotated[int, Path(gt=0)], data: TaskUpdate, session: SessionDep):
    task = session.get(Task, id)

    if task is None:
        raise HTTPException(
                status_code=404,
                detail="Task does not exist"
            )

    update=data.model_dump(exclude_unset=True)

    for column, value in update.items():
        setattr(task, column, value)

    session.commit()
    session.refresh(task)

    return TaskResponse(
            id=task.id,
            name=task.task_name,
            finished=task.finished,
        )
    


@app.delete("/tasks/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_task(id: Annotated[int, Path(gt=0)], session: SessionDep):
    task = session.get(Task, id)

    if task is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail={"message": "task does not exist"}
        )

    session.delete(task)
    session.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)