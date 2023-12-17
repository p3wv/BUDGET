from budget_app import db, login_manager
from flask_login import UserMixin
from enum import Enum

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Enum dla typów transakcji
class TransactionType(Enum):
    EXPENSE = 'Expense'
    INCOME = 'Income'

class User(db.Model, UserMixin):
    
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), nullable=False, unique=True)
    password = db.Column(db.String(80), nullable=False)

# Model transakcji
class Transaction(db.Model):
    
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    amount = db.Column(db.Float, nullable=False)
    type = db.Column(db.Enum(TransactionType), nullable=False)