from typing import Any

from pydantic import BaseModel, Field, model_validator


class TaskCreate(BaseModel):
    task_name: str = Field(min_length=1, max_length=255)
    finished: bool = False 

class TaskUpdate(BaseModel):
    task_name: str | None = None
    finished: bool | None = None

    @model_validator(mode="before")
    @classmethod
    def check_nulls(cls, data: Any) -> Any:
        if isinstance(data, dict) :
            if None in data.values():
                raise ValueError(f"fields cannot be null")
        return data
    
class TaskResponse(BaseModel):
    id: int
    task_name: str
    finished: bool