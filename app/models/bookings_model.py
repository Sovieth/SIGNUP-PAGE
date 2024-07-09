from .. import mongo
from flask import request, redirect, url_for, render_template 
from flask import ObjectId

class MyBookings:
 def Add_booking(bookings):
    return mongo.db.Bookings.insert_one(bookings)
    
    
def get_booking():
    return mongo.db.Bookings.find()
    
   
def confirm():
    return mongo.db.Bookings.find(MyBookings)

def close():
    return mongo.db.Bookings.find(MyBookings)

def Mybookings():
    return mongo.db.Bookings.find(MyBookings)

def delete_booking():
     return mongo.db.Bookings.delete_one({'_id': ObjectId(id)})
 
 
 
 
    


