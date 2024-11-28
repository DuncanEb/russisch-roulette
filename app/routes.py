from flask import Blueprint, render_template, request
from app.game import RussianRoulette

routes = Blueprint('routes', __name__)

@routes.route("/")
def index():
    return render_template("index.html")

@routes.route("/start", methods=["POST"])
def start_game():
    players = request.form.getlist("players")
    game = RussianRoulette()
    game.players = players
    return "Spiel gestartet!"
