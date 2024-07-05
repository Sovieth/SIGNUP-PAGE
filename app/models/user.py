from .. import mongo
from flask import request, redirect, url_for, render_template

class user:
    
    def create_user(data):
        user_id = mongo.db.user.insert_one().inserted_id
        return str(user_id)
    
   
class signup:
    def create_user(details):
     mongo.db.signup.insert_one(details)
     return str(details)
    
    def get_all_signup():
       signup = mongo.db.signup.find_one(signup)
       return list(mongo.db.signup.find({}, {'_id',0}))
   
    def get_all_signup():
       signup = mongo.db.signup.find_one(signup)
       return list(mongo.db.signup.find({}, {'_id',0}))
    
    def get_one_login():
       login = mongo.db.signup.find_one(login)
       return list(mongo.db.signup.find({}, {'_id',0}))