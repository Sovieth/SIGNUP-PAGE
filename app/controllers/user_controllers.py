# /controllers
from flask import request, redirect, url_for, render_template, flash
from ..models.user_model import MyUsers
import re

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
        
        # Validate email format
        email_regex = r'^[\w\.-]+@[\w\.-]+\.\w+$'
        if not re.match(email_regex, email):
            flash('Invalid email format. Please try again.', 'error')
            return redirect(url_for('user.signup'))

        userdata = {"name": name, "surname": surname, "email": email, "password": password}
        if not MyUsers.create_user(userdata):
            flash('Email or username already exists. Please try again with different credentials.', 'error')
            return redirect(url_for('user.signup'))
         
        return render_template("login.html")
    
     # Render the signup form template
     return render_template('Signup.html')
    
def Adminsignup(): 

     if request.method == "POST":
        name = request.form["name"]
        surname = request.form["surname"]
        email = request.form["email"]
        password = request.form["password"]
        
        # Validate email format
        email_regex = r'^[\w\.-]+@[\w\.-]+\.\w+$'
        if not re.match(email_regex, email):
            flash('Invalid email format. Please try again.', 'error')
            return redirect(url_for('user.signup'))

        userdata = {"name": name, "surname": surname, "email": email, "password": password}
        if not MyUsers.create_user(userdata):
            flash('Email or username already exists. Please try again with different credentials.', 'error')
            return redirect(url_for('user.signup'))
        
        return render_template("LoginAdmin.html")
    
     # Render the signup form template
     return render_template('SignupAdmin.html')
 
 
def login():
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]

        userdata = {"email": email, "password": password}
        
        MyUsers.login_user(userdata)
        # return redirect (url_for('user.booking'))
        return redirect(url_for('booking_bp.add_booking'))
    
     # Render the signup form template
    return render_template('login.html')
 
def LoginAdmin():
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]
        
        userdata = {"email": email, "password": password}
        
        MyUsers.LoginAdmin_user(userdata)
        return render_template("AddService.html")
    
     # Render the signup form template
    return render_template('LoginAdmin.html')





