# /controllers
from flask import request, redirect, url_for, render_template, flash
from ..models.bookings_model import MyBookings


# Add booking  
def add_booking():
    if request.method == "POST":
        name = request.form["name"]
        date = request.form["date"]
        time = request.form["time"]
        description = request.form["description"]

        bookings = {
            "name": name,
            "date": date,
            "time": time,
            "description": description
        }

        MyBookings.Add_booking()
    return render_template("Mybooking.htm")
    



    
    
