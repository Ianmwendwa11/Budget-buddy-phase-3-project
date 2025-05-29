from lib.models import create_tables
from lib.models.base import SessionLocal
from lib.models.user import User
from lib.models.transaction import Transaction

create_tables()

def create_user(name, budget):
    session = SessionLocal()
    user = User(name=name, total_budget=budget)
    session.add(user)
    session.commit()
    print(f"User '{name}' created with budget {budget}")
    session.close()

def add_transaction(user_name, description, amount):
    session = SessionLocal()
    user = session.query(User).filter_by(name=user_name).first()
    if not user:
        print(f"User '{user_name}' not found.")
        return
    transaction = Transaction(user_id=user.id, description=description, amount=amount)
    user.total_budget -= amount
    session.add(transaction)
    session.commit()
    print(f"Added transaction: '{description}' for {amount}")
    session.close()

def view_user(user_name):
    session = SessionLocal()
    user = session.query(User).filter_by(name=user_name).first()
    if user:
        print(f"{user.name} - Budget remaining: {user.total_budget}")
    else:
        print(f"No user found with name '{user_name}'")
    session.close()

def view_transactions(user_name):
    session = SessionLocal()
    user = session.query(User).filter_by(name=user_name).first()
    if not user:
        print(f"No user named '{user_name}'")
        return
    transactions = session.query(Transaction).filter_by(user_id=user.id).all()
    for tx in transactions:
        print(f"{tx.description}: {tx.amount}")
    session.close()
