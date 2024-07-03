from flask import Flask
from flask_pymongo import PyMongo
from .config import Config

mongo = PyMongo()



def create_app():
    app = Flask(__name__)
    app.config.from_object(config)
    
    mongo.init_app(app)
    
    
    return app
   