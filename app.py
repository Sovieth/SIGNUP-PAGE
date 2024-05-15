from flask import Flask
from flask import request
from flask_pymongo import PyMongo
from bson import *
from flask import render_template, redirect, url_for

app = Flask(__name__, static_url_path='/static')
app.config["MONGO_URI"] = "mongodb://localhost:27017/Customer"
mongo = PyMongo(app)
db = mongo.db

@app.route('/') 
def index(): 
    # Display the landing page
    return render_template('landing.html') 

# Signup page
@app.route("/signup", methods=["POST", "GET"])
def signup():
    if request.method == "POST":
        name = request.form["name"]
        surname = request.form["surname"]
        email = request.form["email"]
        password = request.form["password"]

        # Check if user already exists
        if db.user.find_one({"email": email}):
            return "User already exists!"

        # Adding user to the database
        user = {"name": name, "surname": surname, "email": email, "password": password}
        db.user.insert_one(user)
        return redirect(url_for('login'))
    return render_template('signup.html')

# Login
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]

        # Fetch user from the database
        user = db.user.find_one({"email": email})
        if user and user["password"] == password:
            return redirect(url_for("get_booking"))
        else:
            return "Invalid credentials"
    return render_template("login.html")

@app.route("/booking", methods=["GET"])
def get_booking():
    booking = list(db.Bookings.find())
    return render_template("booking.html", booking=booking)

from flask import request, redirect, url_for, render_template

@app.route("/booking/add", methods=["POST", "GET"])  
def add_booking():
    if request.method == "POST":
        name = request.form["name"]
        date = request.form["date"]
        time = request.form["time"]
        description = request.form["description"]

        booking = {
            "name": name,
            "date": date,
            "time": time,
            "description": description
        }
        
        db.Bookings.insert_one(booking)
        
        Booking = []

        for i in db.Bookings.find():
            Booking.append(i)
        return render_template('Mybookings.html', bookings=Booking)
    return render_template("booking_form.html")


@app.route("/Mybookings", methods=["POST", "GET"])
def Mybookings():
    bookings = db.Bookings.find()  # Retrieve all documents from the collection

    return render_template("Mybookings.html", booking=bookings)




@app.route("/family", methods=["GET", "POST"])
def family():
    # Code for the family route
    return render_template ("family.html")

@app.route("/wedding", methods=["GET", "POST"])
def wedding():
    # Code for the wedding route
    return render_template ("Wedding.html")

@app.route("/newborn", methods=["GET", "POST"])
def newborn():
    # Code for the newborn route
    return render_template ("newborn.html")

# Booking

@app.route("/booking", methods=["POST", "GET"] )
def getBooking():
     if request.method == 'POST':
          Booking = []

          for i in db.bookings.find():
            Booking.append(i)
            print(Booking)
            
     return render_template("Mybookings.html" , bookings=Booking )


@app.route('/delete', methods=['POST'])
def delete_booking():
    if request.method == "POST":
        id = request.form["id"]
        db.Bookings.delete_one({'_id': ObjectId(id)})
        
        Booking = []

        for i in db.Bookings.find():
            Booking.append(i)
            
    return render_template('Mybookings.html', bookings=Booking)



if __name__ == '__main__':
    app.run(debug=True)