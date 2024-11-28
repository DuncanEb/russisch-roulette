from flask import render_template, request, redirect, url_for
from app import app  # Importiere die Flask-App aus __init__.py
from app.game import Game  # Spiellogik-Klasse
from app.utils import get_players

# Globale Variablen für das Spiel
game = None  # Instanz der Game-Klasse


@app.route("/", methods=["GET", "POST"])
def index():
    """
    Startseite für die Spielerabfrage.
    """
    global game

    if request.method == "POST":
        # Spielernamen aus dem Formular holen
        players = request.form.get("players").splitlines()
        if len(players) < 2:
            return render_template("index.html", error="Es müssen mindestens 2 Spieler angegeben werden.")

        # Neues Spiel initialisieren
        game = Game(players)
        game.setup_game(players)

        return redirect(url_for("play"))

    return render_template("index.html")


@app.route("/play", methods=["GET", "POST"])
def play():
    """
    Spielfluss-Seite.
    """
    global game

    if request.method == "POST":
        # Spieler, der schießen soll, wird aus dem Formular geholt
        current_player = request.form.get("current_player")

        if current_player not in game.players:
            return render_template("play.html", game=game, error=f"{current_player} ist kein gültiger Spieler.")

        # Spieler schießt
        result = game.play_round(current_player)

        # Spiel ist vorbei, wenn nur noch ein Spieler übrig ist
        if game.is_game_over():
            winner = game.get_winner()
            return render_template("play.html", game=game, winner=winner)

    return render_template("play.html", game=game)


@app.route("/restart", methods=["POST"])
def restart():
    """
    Startet das Spiel neu. Optional mit neuen Spielernamen.
    """
    global game

    # Prüfen, ob neue Spielernamen eingegeben wurden
    new_players = request.form.get("players")
    if new_players:
        players = new_players.splitlines()
        if len(players) < 2:
            return redirect(url_for("index"))

        # Neues Spiel mit neuen Spielernamen starten
        game = Game(players)
        game.setup_game(players)
    else:
        # Neues Spiel mit den gleichen Spielern starten
        game.setup_game(game.players)

    return redirect(url_for("play"))
