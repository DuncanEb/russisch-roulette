from flask import Blueprint, render_template, request, redirect, url_for, session
from app.game import RussianRoulette

routes = Blueprint('routes', __name__)
game = None  # Globale Variable für das Spiel

@routes.route("/")
def index():
    """Zeigt die Startseite."""
    players = session.get("players", [])  # Spieler aus der Session laden
    return render_template("index.html", players=players)



@routes.route("/start", methods=["POST"])
def start_game():
    """Startet das Spiel."""
    global game
    players = session.get("players", [])
    if len(players) < 2:  # Sicherstellen, dass mindestens 2 Spieler vorhanden sind
        return redirect(url_for("routes.index"))

    game = RussianRoulette()  # Neues Spiel initialisieren
    game.players = players
    session["message"] = ""  # Nachrichten zurücksetzen
    return redirect(url_for("routes.play"))



@routes.route("/play")
def play():
    """Zeigt den aktuellen Spielstatus."""
    global game
    if not game:
        return redirect(url_for('routes.index'))
    return render_template("play.html", players=game.players)


@routes.route("/play")
def play():
    """Zeigt den aktuellen Spielstatus."""
    global game
    if not game:
        return redirect(url_for("routes.index"))

    message = session.get("message", "")
    return render_template("play.html", players=game.players, message=message)

@routes.route("/shoot", methods=["POST"])
def shoot():
    """Führt einen Schuss aus."""
    global game
    if not game:
        return redirect(url_for("routes.index"))

    current_player = request.form.get("current_player")
    if current_player not in game.players:
        session["message"] = f"❌ Ungültiger Spieler {current_player}."
        return redirect(url_for("routes.play"))

    # Logik für den Schuss
    lost = game.shoot(current_player)
    if lost:
        session["message"] = f"💥 {current_player} hat verloren!"
    else:
        session["message"] = f"🌟 {current_player} hat überlebt!"
    return redirect(url_for("routes.play"))



@routes.route("/add_player", methods=["POST"])
def add_player():
    """Fügt einen neuen Spieler hinzu."""
    player = request.form.get("player").strip()  # Eingabe verarbeiten
    if not player:  # Wenn der Spielername leer ist
        return redirect(url_for("routes.index"))

    # Spieler in der Session speichern
    players = session.get("players", [])  # Vorhandene Spieler laden oder leere Liste
    if player not in players:  # Doppelte Namen vermeiden
        players.append(player)
        session["players"] = players  # Spieler zurück in die Session speichern

    return redirect(url_for("routes.index"))  # Zurück zur Startseite


