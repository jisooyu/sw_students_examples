from userModel import UserModel
from flask_restful import Resource, reqparse

class UserList(Resource):

    parser = reqparse.RequestParser()
    # parser.add_argument('id',
    #     type=int,
    #     required=True,
    #     help="This field cannot be left blank!"
    # )
    parser.add_argument('username',
        type=str,
        required=True,
        help="This field cannot be left blank!"
    )

    def post(self):
        data = UserList.parser.parse_args()
        if UserModel.find_by_username(data['username']):
            return {"message": "User with that username already exists."}, 400
        user = UserModel(**data)
        user.save_to_db()
        return {"message": "User created successfully."}, 201

