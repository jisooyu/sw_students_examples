from db import db
from flask_sqlalchemy import SQLAlchemy
import uuid

class UserModel(db.Model):

    __tablename__= "users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80))

    def __init__(self, id, username):
        self.id = id
        self.username = username

    @classmethod
    def find_by_username(cls, username):
        return cls.query.filter_by(username=username).first()
        
    def save_to_db(self):
        db.session.add(self)
        db.session.commit()
        return {'message': 'data saved'}

