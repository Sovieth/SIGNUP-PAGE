from flask import Blueprint
from ..controllers  import user_controllers

app = Blueprint('user', __name__)

app.route("/")(user_controllers.landing)

# Define the route for the signup page
app.route("/signup", methods = ['POST','GET'])(user_controllers.signup)
app.route("/login", methods=['GET', 'POST'])(user_controllers.login)
app.route("/SignupAdmin", methods = ['POST','GET'])(user_controllers.Adminsignup)
app.route("/login_admin", methods=["GET", "POST"])(user_controllers.LoginAdmin)
