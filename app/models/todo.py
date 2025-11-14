from app.db.base import Base
from sqlalchemy import Column, Integer, String, Boolean, DateTime, func

class ToDo(Base):
    __tablename__ = "todos"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String, index=True)
    is_completed = Column(Boolean, default=False)
    created_at = Column(String, nullable=False, server_default=func.now())
    updated_at = Column(String, nullable=False, server_default=func.now(), onupdate=func.now())