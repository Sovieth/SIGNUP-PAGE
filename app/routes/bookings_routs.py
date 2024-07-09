from flask import Blueprint
from ..controllers  import bookings_controllers

app = Blueprint('bookings', __name__)

app.route("/booking/add", methods=["POST", "GET"]) (bookings_controllers.add_booking) 

app.route("/confirm", methods=["POST", "GET"])(bookings_controllers.confirm)

app.route("/close", methods=["POST", "GET"])(bookings_controllers.close)

app.route("/Mybookings", methods=["POST", "GET"])(bookings_controllers.Mybookings)

app.route("/booking", methods=["POST", "GET"] )(bookings_controllers.get_booking)

app.route('/delete', methods=['POST'])(bookings_controllers.delete_booking)