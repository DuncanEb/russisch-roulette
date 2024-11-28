from app.utils import player_shoot_logic, check_exit, print_revolvers_status, get_players, remove_player
from app.revolver import Revolver
import time

class RussianRoulette:
    def __init__(self, players):
        """
        Initialisiert das Spiel mit einer Liste von Spielern.
        :param players: Liste der Spielernamen
        """
        self.players = players
        self.revolvers = {player: Revolver() for player in players}  # Revolver für jeden Spieler


    def setup_game(self, players=None):
        """
        Rüstet das Spiel mit einer Liste von Spielern aus.
        :param players: Liste der Spielernamen (optional).
        """
        if players is None:
            players = get_players()  # Spieler eingeben, falls nicht übergeben
        self.players = players
        self.revolvers = {player: Revolver() for player in players}

    def play_round(self):
        """
        Spielt eine Runde ab. Wählt den Spieler, führt den Schuss aus und zeigt Status an.
        """
        print(f"\n👥 Verbleibende Spieler: {', '.join(self.players)}")

        # Status der Revolver anzeigen
        print_revolvers_status(self.players, self.revolvers)

        # Spieler auswählen
        current_player = input(f"👉 Wer soll schießen? ({', '.join(self.players)}): ").strip()
        check_exit(current_player)

        if current_player not in self.players:
            print(f"❌ {current_player} ist kein gültiger Spieler. Bitte erneut versuchen.")
            return  # Runde erneut starten

        print(f"\n🔫 {current_player} hebt den Revolver...")

        # 4-Sekunden-Timer für Spannung
        for i in range(4, 0, -1):
            print(f"⏳ {i}...", end="\r", flush=True)
            time.sleep(1)

        # Spieler schießt
        result = player_shoot_logic(current_player, self.players, self.revolvers)

        if result["lost"]:
            print(f"💥 BOOM! {current_player} hat verloren!")
            time.sleep(1)
        else:
            print(f"🌟 Klick! {current_player} hat überlebt!")
            time.sleep(1)

    def is_game_over(self):
        """Prüft, ob das Spiel vorbei ist."""
        return len(self.players) <= 1

    def get_winner(self):
        """Gibt den Gewinner zurück, falls es einen gibt."""
        return self.players[0] if len(self.players) == 1 else None
