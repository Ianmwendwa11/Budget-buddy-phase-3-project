from sqlalchemy import Column, Integer, String, Float
from .base import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True, nullable=False)
    total_budget = Column(Float, default=0.0)

    def __repr__(self):
        return f"<User(name={self.name}, budget={self.total_budget})>"
