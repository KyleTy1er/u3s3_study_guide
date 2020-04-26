
import requests
import bs4
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from bgg_flask_sql.bgg_flask_routes import bgg_flask_routes



# The database should have the following following columns as a minimum: id (integer), name (string), and max_players (integer)

DATABASE_URL = "sqlite:///bgg_db.db"
SECRET_KEY = "super secret key"

def create_app():
    app = Flask(__name__)

    app.config["SECRET_KEY"] = SECRET_KEY
    app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE_URL
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.init_app(app)
    migrate.init_app(app, db)

    app.register_blueprint(bgg_flask_routes)
    return app

