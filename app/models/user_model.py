from .. import mongo
from flask import request, redirect, url_for, render_template

class MyUsers:
    
   
    def login_user(userdata):
        mongo.db.user.insert_one(userdata)
        return str("user data")
    
    
    def LoginAdmin_user(userdata):
        mongo.db.User_Admin.insert_one(userdata)
        return str("user data")
    
   
    def create_user(userdata):
        existing_user = MyUsers.find_user_by_name_or_email(userdata['name'], userdata['email'])
        if existing_user:
            return False  # User already exists
        else:
            # Insert the new user into the database
            mongo.db.user.insert_one(userdata)
            return True  # User created successfully

  
    def find_user_by_name_or_email(name,email ):
        return mongo.db.user.find_one({'$or': [{'name':name}, {'email': [email]}]})

  
    def find_user_by_email_and_password(name, password):
        return mongo.db.user.find_one({'name': name, 'password': password})

 
    def get_user_by_email(email):
        return mongo.db.user.find_one({'email': email}) 