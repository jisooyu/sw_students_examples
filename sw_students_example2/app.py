from flask import Flask
from flask_restful import Api
from userResource import UserList, User # add User
from flask_jwt import JWT
from security import authenticate, identity # add this line


app = Flask(__name__)
app.secret_key = "my precious Holy Mother"
app.config['SQLALCHEMY_DATABASE_URI'] ="sqlite:///data.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
api = Api(app)

@app.before_first_request
def create_tables():
    db.create_all()

jwt = JWT(app, authenticate, identity) # add this line

api.add_resource(UserList, '/register')
api.add_resource(User, '/username/<string:username>') # add this line

if __name__ == '__main__':
    from db import db
    db.init_app(app)
    app.run(debug=True, host='0.0.0.0')
