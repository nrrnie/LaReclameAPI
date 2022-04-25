from api import db
from datetime import datetime


class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255), nullable=False, unique=True)
    password = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), nullable=False, unique=True)
    registered = db.Column(db.DATETIME, nullable=False, default=datetime.now)

    def get_json(self):
        return {
            'id': self.id,
            'username': self.username,
            'email': self.email,
            'registered': self.registered
        }

class Items(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    author_username = db.Column(db.String(255), nullable=False)
    created = db.Column(db.DATETIME, nullable=False, default=datetime.now)
    title = db.Column(db.String(255), nullable=False)
    body = db.Column(db.String(255), nullable=False)
    is_active = db.Column(db.Boolean, nullable=False, default=True)

    def get_json(self):
        return {
            'id': self.id,
            'author': self.author_username,
            'created': self.created, 
            'title': self.title,
            'body': self.body,
            'is_active': self.is_active
        }