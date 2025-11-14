from fastapi import APIRouter
from app.services.todo_service import create_todo_service, get_all_todos_service, get_todo_by_id_service, update_todo_service, delete_todo_service
from app.db.sessions import get_db
from sqlalchemy.orm import Session
from app.schemas.todo_schema import TodoCreate, TodoResponse, TodoUpdate
from fastapi import Depends
from typing import List


todo_router = APIRouter(prefix="/v1/todo", tags=["ToDo"])

@todo_router.post("/", response_model=TodoResponse)
def create_todo(payload:TodoCreate, db:Session = Depends(get_db)):
    return create_todo_service(payload, db)


@todo_router.get("/", response_model=List[TodoResponse])
def get_todos(db:Session = Depends(get_db)):
    return get_all_todos_service(db)

@todo_router.get("/{todo_id}",response_model=TodoResponse)
def get_todo_by_id(todo_id:int, db:Session = Depends(get_db)):
    return get_todo_by_id_service(todo_id, db)

@todo_router.put("/{todo_id}", response_model=TodoResponse)
def update_todo(todo_id:int, payload:TodoUpdate, db:Session = Depends(get_db)):
    return update_todo_service(todo_id, payload, db)

@todo_router.delete("/{todo_id}", response_model=TodoResponse)
def delete_todo(todo_id:int,db:Session=Depends(get_db)):
    return delete_todo_service(todo_id, db)