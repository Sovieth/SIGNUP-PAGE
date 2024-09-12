# /controllers
from bson import ObjectId
from flask import request, redirect, url_for, render_template, flash
from ..models.bookings_model import Bookings

# Add booking
def add_booking():
    if request.method == "POST":
        # Retrieve form data
        name = request.form["name"]
        date = request.form["date"]
        time = request.form["time"]
        description = request.form["description"]
        
        # Create a booking dictionary
        booking = {
            "name": name,
            "date": date,
            "time": time,
            "description": description
        }
    
        Bookings.Add_booking(booking)
        return redirect(url_for('booking_bp.confirm'))
    return render_template("booking.html")

def close():
    Booking = []
    for i in Bookings.display_booking():
        Booking.append(i)
    return render_template('Mybookings.html', bookings=Booking)

def confirm():
 return render_template('confirm.html')

def delete_booking():
    if request.method == "POST":
       id = request.form["id"]
       service_id = ObjectId(id)
       Bookings.delete_booking(service_id)

    return redirect(url_for('booking_bp.close'))

def  edit1_booking():
    if request.method == "POST":
        # Retrieve form data
        id = request.form["id"]
        name = request.form["name"]
        date = request.form["date"]
        time = request.form["time"]
        description = request.form["description"]
        print("in edd",id)
        # Create a booking dictionary
        booking = {
            "name": name,
            "date": date,
            "time": time,
            "description": description
        }
        id = ObjectId(id)
        
        Bookings.edit_booking1(id, booking)
        
        return redirect(url_for('booking_bp.close'))
    else:
         return render_template('Mybookings.html', bookings=booking)

def edit_booking():
    if request.method == "POST":
        # Retrieve form data
        id = request.form["id"]
        name = request.form["name"]
        date = request.form["date"]
        time = request.form["time"]
        description = request.form["description"]
        print(id)
        print(name)
        print(date)
        print(description)
        print(time)
        return render_template('EditService.html', id=id, name=name, date=date, time=time, description=description)


