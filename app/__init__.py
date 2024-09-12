from flask import Flask
from flask_pymongo import PyMongo
from .config import Config

mongo = PyMongo()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    
    mongo.init_app(app)
    
    # regiter your routes
    with app.app_context():
        from .routes import user_routes, AddService_routes, bookings_routes,Reviews_routes
        
    app.register_blueprint(user_routes.app)
    app.register_blueprint(bookings_routes.app)
    app.register_blueprint(AddService_routes.app)
    app.register_blueprint(Reviews_routes.app)
    
    return app