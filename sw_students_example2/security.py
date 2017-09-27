# https://www.udemy.com/rest-api-flask-and-python/learn/v4/t/lecture/5960168?start=0
# Authentication and Logging in - Part 1

from werkzeug.security import safe_str_cmp # needed due to different versions of Python
from userModel import UserModel

def authenticate(username, password): # to get username and password from the end points 
    user = UserModel.find_by_username(username)
    # if user and user.password == password:
    if user and safe_str_cmp (user.password, password): #  to check if username and password match
        return user # return user to be used to generate jwt token

def identity (payload): # whenever the endpoint requests, we use identity function to authenticate 
    user_id = payload['identity'] # to get the user_id from the payload
    return UserModel.find_by_id(user_id) # to retrieve the user object using user_id