# /controllers
from flask import request, redirect, url_for, render_template, flash

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


        # Check if user already exists
        if user.find_one({"email": email}):
            return "User already exists!"

        # Adding user to the database
        user = {"name": name, "surname": surname, "email": email, "password": password}
        user.insert_one(user)
        return redirect(url_for('login'))
    
     # Render the signup form template
     return render_template('signup.html')
 
#  SignupAdmin page

def SignupAdmin():
    if request.method == "POST":
        name = request.form["name"]
        surname = request.form["surname"]
        email = request.form["email"]
        password = request.form["password"]

        # Check if user already exists
        if user.find_one({"email": email}):
            return "User already exists!"

        # Adding user to the database
        user = {"name": name, "surname": surname, "email": email, "password": password}
        user.insert_one(user)
        return redirect(url_for('LoginAdmin'))
    return render_template('SignupAdmin.html')

def login():
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]

        # Fetch user from the database
        user = user.find_one({"email": email})
        if user and user["password"] == password:
            return redirect(url_for("get_booking"))
        else:
            return "Invalid credentials"
    return render_template("login.html")


 

