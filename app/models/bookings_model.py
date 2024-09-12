from bson import ObjectId
from .. import mongo

class Bookings:
    def Add_booking(booking):
        return mongo.db.Bookings.insert_one(booking)
    
    def display_booking():
        return mongo.db.Bookings.find()
    
    def confirm():
        return mongo.db.Bookings.find()
    
    def delete_booking(delete_id):
        return mongo.db.Bookings.delete_one({"_id": ObjectId(delete_id)})
    
    def edit_booking1(id, booking):
        return mongo.db.Bookings.update_one({"_id": ObjectId(id)}, {"$set": booking})

 


