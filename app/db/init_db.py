from .base import Base
from .sessions import engine


def init_db():
    print("Creating database tables if not exits...")
    Base.metadata.create_all(bind=engine)