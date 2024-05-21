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

# SignupAdmin page
@app.route("/SignupAdmin", methods=["POST", "GET"])
def SignupAdmin():
    if request.method == "POST":
        name = request.form["name"]
        surname = request.form["surname"]
        email = request.form["email"]
        password = request.form["password"]

        # Check if user already exists
        if db.Admin.find_one({"email": email}):
            return "User already exists!"

        # Adding user to the database
        user = {"name": name, "surname": surname, "email": email, "password": password}
        db.Admin.insert_one(user)
        return redirect(url_for('LoginAdmin'))
    return render_template('SignupAdmin.html')


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

# LoginAdmin
@app.route("/LoginAdmin", methods=["GET", "POST"])
def LoginAdmin():
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]

        # Fetch user from the database
        user = db.Admin.find_one({"email": email})
        if user and user["password"] == password:
            return redirect(url_for("get_AddService"))
        else:
            return "Invalid credentials"
    return render_template("LoginAdmin.html")
#Services
@app.route("/services", methods=["GET"])
def get_AddService():
    service = db.services.find()
    return render_template("AddService.html", service=service)

#Add Service
@app.route('/AddService', methods=['POST'])
def AddService():
    category = request.form['category']
    price = request.form['price']
    description = request.form['description']  # Use lowercase 'description' for consistency
    image = request.form['image']
    
    service = {'category': category, 'price': price, 'description': description, 'image': image}
    
    try:
        db.services.insert_one(service)
        # If insertion is successful, render the landing page
        return render_template("landing.html", service = service)
    except Exception as e:
        # If insertion fails, print the error and return an error message
        print(f"Error inserting service: {e}")
        return 'Form submission failed', 500
    
   

# Add booking
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


# services

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

@app.route('/Edit_Service', methods=['POST'])
def edit_booking():
    if request.method == "POST":
        id = request.form["id"]
        name = request.form["name"]
        date = request.form["date"]
        time = request.form["time"]

        return render_template('EditService.html', id=id,name=name, date=date, time=time)

@app.route('/Edit_Service1', methods=['POST'])
def edit1_booking():
    if request.method == "POST":
        id = request.form["id"]
        name = request.form["name"]
        date = request.form["date"]
        time = request.form["time"]
        db.Bookings.update_one( { "_id":  ObjectId(id)}, { '$set': { "name": name, "date":date, "time":time} } ) 
        Booking = []

        for i in db.Bookings.find():
            Booking.append(i)
            
    return render_template('Mybookings.html', bookings=Booking)




# add services


if __name__ == '__main__':
    app.run(debug=True)