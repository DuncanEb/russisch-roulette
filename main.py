from app.game import RussianRoulette
from app.utils import get_players, check_exit

def main():
    players = None  # Initialisiere die Spieler-Liste

    while True:
        print("🎲 Willkommen zum Russischen Roulette! 🎲")

        # Frage nur nach Spielern, wenn keine existieren oder neue Namen gewünscht sind
        if players is None:
            players = get_players()

        # Spiel initialisieren
        game = RussianRoulette(players)
        game.setup_game(players)

        print(f"\n✅ {len(players)} Spieler treten an: {', '.join(players)}")
        print("=" * 50)

        # Hauptspiel-Schleife
        while not game.is_game_over():
            game.play_round()

        # Gewinner anzeigen
        winner = game.get_winner()
        if winner:
            print(f"\n🏆 {winner} ist der Gewinner! 🎉")
        else:
            print("❌ Kein Gewinner, alle Spieler sind ausgeschieden.")

        # Frage, ob erneut gespielt werden soll
        replay = input("\n🔁 Möchten Sie eine neue Runde spielen? (ja/nein): ").strip().lower()
        check_exit(replay)

        if replay != "ja":
            print("\n🎮 Spiel beendet. Bis zum nächsten Mal!")
            break

        # Frage, ob Namen geändert werden sollen
        change_names = input("❓ Möchten Sie die Spielernamen ändern? (ja/nein): ").strip().lower()
        check_exit(change_names)

        if change_names == "ja":
            players = get_players()  # Nur jetzt die Spieler neu abfragen


if __name__ == "__main__":
    main()
