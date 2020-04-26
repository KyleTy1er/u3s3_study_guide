
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()

migrate = Migrate()

class Game(db.Model):
    id = db.Column(db.BigInteger, primary_key=True)
    name = db.Column(db.String(128), nullable=False)
    max_players = db.Column(db.Integer)