from flask import Blueprint, jsonify, request, render_template
import requests
import bs4
from bgg_flask_sql.models import Game, db, migrate

admin_routes = Blueprint("bgg_flask_routes", __name__)
bgg_flask_routes = Blueprint("bgg_flask_routes", __name__)


@bgg_flask_routes.route("/<game_id>", methods=['GET', 'POST', 'PULL'])
def get_game_data(game_id):
    game_id = game_id
    url = 'https://www.boardgamegeek.com/xmlapi/boardgame/' + str(game_id)
    result = requests.get(url)
    soup = bs4.BeautifulSoup(result.text, features='lxml')
    game_name = (soup.find('name').text)
    max_players = (soup.find('maxplayers').text)
    return render_template("temp.html", max_players=max_players, game_name=game_name, game_id=game_id)


@bgg_flask_routes.route("/store/<game_id>")
def store_game_data(game_id):
    game_id = game_id
    url = 'https://www.boardgamegeek.com/xmlapi/boardgame/' + str(game_id)
    result = requests.get(url)
    soup = bs4.BeautifulSoup(result.text, features='lxml')
    db_game = Game.query.get(soup.find('name').text)
    db_game_id.id = game_id
    db_game.name = (db.find('name').text)
    db_max_players.max_players = (db.find('maxplayers').text)
    db.session.add(db_game)
    db.session.commit()

    # db_game = Game.db_game()
    # db_game.name = game_name
    # db_game.max_players = max_players
    # db.session.add(db_game)
    # db.session.commit()