from flask import Blueprint
from ..controllers  import Reviews_controllers

app = Blueprint('review_bp', __name__)

app.route('/review', methods=['GET', 'POST'])(Reviews_controllers.review)
app.route('/review_display12', methods=['GET', 'POST'])(Reviews_controllers.review_display)