
from app.models.todo import ToDo


def create_todo_service(payload, db):
    new_todo = ToDo(**payload.model_dump())
    db.add(new_todo)
    db.commit()
    db.refresh(new_todo)
    return new_todo


def get_all_todos_service(db):
    todos = db.query(ToDo).all()
    return todos


def get_todo_by_id_service(todo_id, db):
    todo = db.query(ToDo).filter(ToDo.id == todo_id).first()
    return todo

def update_todo_service(todo_id, payload, db):
    todo = db.query(ToDo).filter(ToDo.id == todo_id).first()
    if todo:
        for key, value in payload.model_dump().items():
            setattr(todo, key, value)
        db.commit()
        db.refresh(todo)
    return todo


def delete_todo_service(todo_id, db):
    todo = db.query(ToDo).filter(ToDo.id == todo_id).first()
    if todo:
        db.delete(todo)
        db.commit()
    return todo