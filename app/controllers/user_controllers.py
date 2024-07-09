# /controllers
from flask import request, redirect, url_for, render_template, flash
from ..models.user_model import MyUsers


def landing(): 
    # Display the landing page
    return render_template("landing.html") 

# Signup page
def signup(): 

     if request.method == "POST":
        name = request.form["name"]
        surname = request.form["surname"]
        email = request.form["email"]
        password = request.form["password"]

        userdata = {"name": name, "surname": surname, "email": email, "password": password}
        
        # check if user exists using email
       
         
        MyUsers.sign_up_user(userdata)
        return render_template("login.html")
    
     # Render the signup form template
     return render_template('signup.html')
 
def Adminsignup(): 

     if request.method == "POST":
        name = request.form["name"]
        surname = request.form["surname"]
        email = request.form["email"]
        password = request.form["password"]

        userdata = {"name": name, "surname": surname, "email": email, "password": password}
        
        MyUsers.Adminsign_up_user(userdata)
        return render_template("login.html")
    
     # Render the signup form template
     return render_template('Signup.html')
 
 
def login():
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]
        
        
        userdata = {"email": email, "password": password}
        
        MyUsers.sign_up_user(userdata)
        return render_template("login.html")
    
     # Render the signup form template
    return render_template('login.html')
 
def LoginAdmin():
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]
        
        
        userdata = {"email": email, "password": password}
        
        MyUsers.LoginAdmin_user(userdata)
        return render_template("LoginAdmin.htm")
    
     # Render the signup form template
    return render_template('LoginAdmin.html')

