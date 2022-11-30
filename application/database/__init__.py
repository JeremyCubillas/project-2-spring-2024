"""
Database Initialization and Models
"""
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class User(db.Model):
    """User Model"""
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128))
    password = db.Column(db.String(128))
    email = db.Column(db.String(128))
    phone = db.Column(db.String(128))
    address = db.Column(db.String(128))

    @classmethod
    def all(cls):
        return cls.query.all()

    @classmethod
    def find_user_by_email(cls, email):
        return cls.query.filter(cls.email == email).first()

    @classmethod
    def find_user_by_id(cls, user_id):
        return cls.query.filter(cls.id == user_id).first()

    @classmethod
    def record_count(cls):
        return cls.query.count()
