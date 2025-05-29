from .base import Base, engine
from .user import User
from .transaction import Transaction

def create_tables():
    Base.metadata.create_all(engine)
