

from flask import Blueprint, jsonify, request, render_template

admin_routes = Blueprint("bgg_flask_routes", __name__)
home_routes = Blueprint("bgg_flask_routes", __name__)

@admin_routes.route("/reset", methods=['GET', 'POST'])
def reset_db():
    print("RESET ROUTE...")
    print("FORM DATA:", dict(request.form))
    print(type(db))
    db.drop_all()
    db.create_all()
    return render_template("reset_db.html", db=db)

def store_twitter_user_data(screen_name):
    api = api_client()
    twitter_user = api.get_user(screen_name)
    #statuses = api.user_timeline(screen_name, tweet_mode="extended", count=150, exclude_replies=True, include_rts=False)
    statuses = api.user_timeline(screen_name, tweet_mode="extended", count=150)
    #return jsonify({"user": user._json, "tweets": [s._json for s in statuses]})

    db_user = User.query.get(twitter_user.id) or User(id=twitter_user.id)
    db_user.screen_name = twitter_user.screen_name
    db_user.name = twitter_user.name
    db_user.location = twitter_user.location
    db_user.followers_count = twitter_user.followers_count
    db.session.add(db_user)
    db.session.commit()

@twitter_routes.route("/users.json")
def list_users():
    # assigns the result of querying the user table from the sqlite database that is assigned in the __init__ file "kyle_twitter_db.db" to
    # the variable db_users
    db_users = User.query.all()

    users = parse_records(db_users)
    return jsonify(users)

@home_routes.route("/")
def index():
    print("VISITED THE HOME PAGE")
    return render_template("prepare_to_predict.html")

@home_routes.route("/")
def index():
    print("VISITED THE HOME PAGE")
    return render_template("prepare_to_predict.html")