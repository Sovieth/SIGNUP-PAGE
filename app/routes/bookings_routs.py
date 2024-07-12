from flask import Blueprint
from ..controllers  import bookings_controllers

app = Blueprint('bookings', __name__)

app.route("/booking/add", methods=["POST", "GET"]) (bookings_controllers.add_booking) 

app.route("/booking", methods=["POST", "GET"] )(bookings_controllers.get_booking)
