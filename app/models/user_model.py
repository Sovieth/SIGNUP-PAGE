from .. import mongo
from flask import request, redirect, url_for, render_template

class MyUsers:
    
    def sign_up_user(userdata):
        mongo.db.user.insert_one(userdata)
        return str("user data")
    
    def login_user(userdata):
        mongo.db.user.insert_one(userdata)
        return str("user data")
    
    def Adminsign_up_user(userdata):
        mongo.db.user.insert_one(userdata)
        return str("user data")
    
    def LoginAdmin_user(userdata):
        mongo.db.user.insert_one(userdata)
        return str("user data")
    
    def login_user(email, password): 
        return mongo.db.user.find_one({"email": email, "password": password})