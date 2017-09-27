from flask import Flask
from flask_restful import Api
from userResource import UserList

app = Flask(__name__)
app.secret_key = "my precious Holy Mother"
app.config['SQLALCHEMY_DATABASE_URI'] ="sqlite:///data.db"

api = Api(app)
api.add_resource(UserList, '/register')

if __name__ == '__main__':
    from db import db
    db.init_app(app)
    app.run(debug=True, host='0.0.0.0')
