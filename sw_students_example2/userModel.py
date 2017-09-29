from db import db
from flask_sqlalchemy import SQLAlchemy


class UserModel(db.Model):

    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80))
    password = db.Column(db.String(80)) # add this line

    def __init__(self, username, password):
        self.username = username
        self.password = password # add this line

    @classmethod
    def find_by_username(cls, username):
        return cls.query.filter_by(username=username).first()
        
    def save_to_db(self):
        db.session.add(self)
        db.session.commit()
        return {'message': 'data saved'}

    def json(self): # add this line
        return {'username': self.username}

    @classmethod # add this line
    def find_by_id(cls, id):
        return cls.query.filter_by(id = id).first()