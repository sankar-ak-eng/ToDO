from pydantic import BaseModel
from datetime import datetime

class TodoBase(BaseModel):
    title: str
    is_completed: bool = False
    description: str | None = None
  

class TodoCreate(TodoBase):
    pass                        

class TodoUpdate(TodoBase):
    title: str | None = None
    is_completed: bool | None = None

class TodoResponse(TodoBase):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True