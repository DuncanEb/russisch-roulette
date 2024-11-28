from app.revolver import Revolver
from app.utils import check_exit, get_players, print_revolvers_status
import time

class RussianRoulette:
    def __init__(self):
        self.players = []

    def start_game(self):
        """Startet das Spiel."""
        print("🎲 Willkommen zum Russischen Roulette! 🎲")

        # Spieler einlesen mit ausgelagerter Funktion
        self.players = get_players()

        print(f"\n✅ {len(self.players)} Spieler treten an: {', '.join(self.players)}")
        print("=" * 50)

        # Initialisiere Revolver für jeden Spieler
        revolvers = {player: Revolver() for player in self.players}

        # Spiel-Schleife
        while len(self.players) > 1:
            print(f"\n👥 Verbleibende Spieler: {', '.join(self.players)}")

            # Statusanzeige der Revolver mit ausgelagerter Funktion
            print_revolvers_status(self.players, revolvers)

            # Spieler auswählen
            current_player = input("👉 Wer soll als nächstes schießen? (Name eingeben): ").strip()
            check_exit(current_player)

            if current_player not in self.players:
                print(f"❌ {current_player} ist kein gültiger Spieler. Bitte erneut versuchen.")
                continue

            # Spieler schießt
            print(f"\n🔫 {current_player} hebt den Revolver...")
            time.sleep(1)

            # Prüfe, ob der Spieler überlebt
            if revolvers[current_player].shoot():
                print(f"💥 BOOM! {current_player} hat verloren!")
                self.players.remove(current_player)
                del revolvers[current_player]
            else:
                print(f"🌟 Klick! {current_player} hat überlebt!")

            time.sleep(1)

        # Spielende
        if len(self.players) == 1:
            print(f"\n🏆 {self.players[0]} ist der Gewinner! 🎉")
        else:
            print("❌ Kein Gewinner. Alle Spieler sind ausgeschieden.")
