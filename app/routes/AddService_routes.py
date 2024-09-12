from flask import Blueprint
from ..controllers  import AddService_controllers

app = Blueprint('service_bp', __name__)

app.route('/AddService', methods=['POST','GET'])(AddService_controllers.AddService)
app.route('/services', methods=['POST','GET'])(AddService_controllers.services)
app.route('/Edit_Service1', methods=['POST'])(AddService_controllers.edit1_service)
app.route('/delete_service', methods=['GET','POST'])(AddService_controllers.delete_service)
app.route('/Edit_Service', methods=['POST'])(AddService_controllers.edit_service)



