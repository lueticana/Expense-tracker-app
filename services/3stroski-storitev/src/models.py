from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

db = SQLAlchemy()

class Expense(db.Model):
    __tablename__ = 'stroski'
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String, nullable=False)
    amount = db.Column(db.Float, nullable=False)