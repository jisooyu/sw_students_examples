# https://github.com/schoolofcode-me/rest-api-sections/tree/master/section6
# https://www.udemy.com/rest-api-flask-and-python/learn/v4/t/lecture/6020504?start=0
import os
from flask import Flask
from flask_restful import Api
from flask_jwt import JWT

from security import authenticate, identity
from resources.user import UserRegister
from resources.item import Item, ItemList
from resources.store import Store, StoreList

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL','sqlite:///data.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False # to turn off Flask SqlAlchemy tracker 
app.secret_key = 'jose'
api = Api(app)

jwt = JWT(app, authenticate, identity) #from /auth, we get the jwt to use where @jwt_required 

api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')

api.add_resource(UserRegister, '/register')

if __name__ == '__main__':
	from db import db # to place the import statement here to prevent the circular import
	db.init_app(app) 
	app.run(debug=True) 