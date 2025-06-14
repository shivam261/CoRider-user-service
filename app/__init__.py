from flask import Flask
from dotenv import load_dotenv
from flask_pymongo import PyMongo
from flask_caching import Cache
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
import os

load_dotenv("development.env")

mongo = PyMongo()
cache = Cache()
limiter = Limiter(key_func=get_remote_address)

def create_app():
    app = Flask(__name__)
    app.config["MONGO_URI"] = os.getenv("MONGO_URI", "mongodb://127.0.0.1:27017/corider")

    app.config["CACHE_TYPE"] = "simple"
    print("Using MONGO_URI:", app.config["MONGO_URI"])
    mongo.init_app(app)
    cache.init_app(app)
    limiter.init_app(app)

    # Register blueprints
    from app.routes import user_routes
    app.register_blueprint(user_routes.user_bp)

    return app
