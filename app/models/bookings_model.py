from .. import mongo
from flask import request, redirect, url_for, render_template 
from flask import ObjectId

class MyBookings:
 def Add_booking(bookings):
    return mongo.db.Bookings.insert_one(bookings)
      
def get_booking():
    return mongo.db.Bookings.find()
    
 
 
 
    


