from flask import Flask
from pymongo import MongoClient
from flask_login import LoginManager

mongo = None  # Will hold the MongoDB client
DB_NAME = "fastcars"


def create_app():
    global mongo
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'bingo is a dog'
    app.config["MONGO_URI"] = f"mongodb://localhost:27017/{DB_NAME}"

    # Set up PyMongo client
    mongo = MongoClient(app.config["MONGO_URI"])[DB_NAME]

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    from .models import User

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(user_id):
        return User.get_by_id(user_id)

    # Attach mongo to app for access in models
    app.mongo = mongo

    return app