from flask import Blueprint
from ..controllers  import bookings_controllers

app = Blueprint('booking_bp', __name__)

app.route("/booking", methods=["POST", "GET"])(bookings_controllers.add_booking)   
app.route("/display_booking", methods=["POST", "GET"])(bookings_controllers.close)
app.route("/booking_confirmed", methods=["POST", "GET"])(bookings_controllers.confirm)
app.route('/delete', methods=['POST'])(bookings_controllers.delete_booking)
app.route('/Edit_Booking1', methods=['POST'])(bookings_controllers.edit1_booking)
app.route('/Edit_Booking', methods=['POST'])(bookings_controllers.edit_booking)





