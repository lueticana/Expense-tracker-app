from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

db = SQLAlchemy()

class Group(db.Model):
    __tablename__ = 'skupine'
    id = db.Column(db.Integer, primary_key=True)
    group_name = db.Column(db.String(80), nullable=False, unique= True)

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.group_name
        }

class GroupMember(db.Model):
    __tablename__ = 'clani'
    id = db.Column(db.Integer, primary_key=True)
    group_id = db.Column(db.Integer, db.ForeignKey('skupine.id'), nullable=False)
    user_id = db.Column(db.Integer, nullable=False)
