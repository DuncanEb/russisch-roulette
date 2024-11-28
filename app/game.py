from app.utils import player_shoot_logic, check_exit, print_revolvers_status, get_players, remove_player
from app.revolver import Revolver
import time

class Game:
    def __init__(self, players):
        self.players = players
        self.revolvers = {}
        self.original_players = players[:]  # Originale Spieler speichern
        self.setup_game(players)

    def setup_game(self, players):
        """
        Initialisiert das Spiel mit einer Liste von Spielern.
        :param players: Liste der Spielernamen
        """
        self.players = players[:]
        self.revolvers = {player: Revolver() for player in players}

    def play_round(self, current_player):
        """
        Führt eine Schussaktion durch und gibt das Ergebnis zurück.
        :param current_player: Spieler, der schießt
        :return: Dictionary mit den Ergebnissen (ob verloren oder nicht)
        """
        if self.revolvers[current_player].shoot():
            # Spieler verliert
            self.players.remove(current_player)
            del self.revolvers[current_player]
            return {"lost": True, "player": current_player}
        return {"lost": False, "player": current_player}

    def is_game_over(self):
        return len(self.players) <= 1

    def get_winner(self):
        return self.players[0] if len(self.players) == 1 else None

    def reset_to_original_players(self):
        """
        Setzt die Spieler auf die ursprüngliche Liste zurück.
        """
        self.setup_game(self.original_players)

