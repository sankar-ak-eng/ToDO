from fastapi import FastAPI
from app.db.init_db import init_db
from app.api.v1.todo_routers import todo_router

app = FastAPI()




@app.on_event("startup")
def on_startup():
    init_db()


# Include Routers
app.include_router(todo_router, prefix="/api", tags=["Todos"])

@app.get("/")
def read_root():
    return {"message": "Welcome to the ToDo API"}