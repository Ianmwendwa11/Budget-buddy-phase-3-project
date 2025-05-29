from sqlalchemy import Column, Integer, String, Float, ForeignKey
from .base import Base

class Transaction(Base):
    __tablename__ = "transactions"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    description = Column(String)
    amount = Column(Float)

    def __repr__(self):
        return f"<Transaction(user_id={self.user_id}, desc='{self.description}', amount={self.amount})>"
