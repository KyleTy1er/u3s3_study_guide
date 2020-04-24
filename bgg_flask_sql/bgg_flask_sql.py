
import requests
import bs4
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

migrate = Migrate()

class User(db.Model):
    id = db.Column(db.BigInteger, primary_key=True)
    screen_name = db.Column(db.String(128), nullable=False)
    name = db.Column(db.String)
    location = db.Column(db.String)
    followers_count = db.Column(db.Integer)