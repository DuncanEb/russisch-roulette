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

        # Validierung
        if len(players) < 2:
            return render_template("index.html", error="Es müssen mindestens 2 Spieler angegeben werden.")
        if any(not player.strip() for player in players):  # Leere Namen verhindern
            return render_template("index.html", error="Spielernamen dürfen nicht leer sein.")
        if len(players) != len(set(player.strip() for player in players)):  # Doppelte Namen verhindern
            return render_template("index.html", error="Spielernamen müssen eindeutig sein.")

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
        # Spieler, der schießen soll
        current_player = request.form.get("current_player")

        if current_player not in game.players:
            return render_template("play.html", game=game, error=f"{current_player} ist kein gültiger Spieler.")

        # Spieler schießt
        result = game.play_round(current_player)

        # Spiel ist vorbei
        if game.is_game_over():
            winner = game.get_winner()
            revolvers_status = {
                player: 6 - game.revolvers[player].current_position
                for player in game.players
            }
            return render_template("play.html", game=game, winner=winner, revolvers=revolvers_status, result=result)

        # Status der Revolver
        revolvers_status = {
            player: 6 - game.revolvers[player].current_position
            for player in game.players
        }

        return render_template("play.html", game=game, revolvers=revolvers_status, result=result)

    # Initial GET-Anfrage
    revolvers_status = {
        player: 6 - game.revolvers[player].current_position
        for player in game.players
    }
    return render_template("play.html", game=game, revolvers=revolvers_status)


@app.route("/restart", methods=["POST"])
def restart():
    """
    Startet das Spiel neu. Optional mit neuen Spielernamen.
    """
    global game

    # Prüfen, ob neue Spielernamen eingegeben wurden
    new_players = request.form.get("players")  # Eingabe aus dem Textfeld
    if new_players:
        players = new_players.splitlines()  # Neue Spielernamen verarbeiten
        if len(players) < 2:
            # Fehler, wenn weniger als 2 Spieler eingegeben wurden
            return render_template("play.html", game=game, error="Es müssen mindestens 2 Spieler angegeben werden.")
        # Neues Spiel mit neuen Spielern
        game = Game(players)
    else:
        # Neues Spiel mit ursprünglichen Spielern
        game.reset_to_original_players()

    return redirect(url_for("play"))


