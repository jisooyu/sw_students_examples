# class User does not contain any methods(api) to respond to users' requests unlike RUST api
# So class User is "helper" function  merely finding username and pw. 
import sqlite3
from db import db

class UserModel(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80))
    password = db.Column(db.String(80))

    # no need for id as argument since it is automaticallly incremented by SQALCHEMY
    def __init__(self, username, password): 
        self.username = username
        self.password = password

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def find_by_username(cls, username):
        # the first arguement username is table name, the second is the arguement username
        return cls.query.filter_by(username=username).first() 

    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id = _id).first()

