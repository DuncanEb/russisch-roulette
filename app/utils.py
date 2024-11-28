def check_exit(input_text):
    """Überprüft, ob der eingegebene Text das geheime Wort 'exit' enthält."""
    if input_text.strip().lower() == "exit":
        print("\n🎮 Spiel wurde abgebrochen. Bis zum nächsten Mal! 🙌")
        exit()


# def get_players(self):
#     # Spielerregistrierung
#     print("👥 Spieler eingeben:")
#     while True:
#         player_name = input("➤ Spielername: ").strip()
#         check_exit(player_name)
#         if player_name == "":
#             if len(self.players) < 2:
#                 print("❌ Mindestens 2 Spieler erforderlich.")
#                 continue
#             break
#         self.players.append(player_name)


# def print_revolvers_status(self, revolvers):
#     """Zeige den Status aller Revolver an."""
#     print("\n🔫 Revolverstatus:")
#     for player, revolver in revolvers.items():
#         print(f"  {player}: {revolver.remaining_shots()} Schuss verbleibend")
#     print("-" * 50)


def get_players():
    """Lässt den Benutzer die Spieler eingeben."""
    players = []
    print("👥 Bitte die Namen der Spieler eingeben (einen Namen pro Zeile).")
    print("🚪 Drücke Enter ohne Eingabe, um die Eingabe zu beenden.")
    while True:
        player_name = input("➤ Spielername: ").strip()
        check_exit(player_name)
        if player_name == "":
            if len(players) < 2:
                print("❌ Es müssen mindestens 2 Spieler teilnehmen.")
                continue
            break
        players.append(player_name)
    return players


def print_revolvers_status(players, revolvers):
    """Zeigt den Status der Revolver für alle Spieler an."""
    print("\n🔫 Revolverstatus:")
    for player in players:
        remaining_shots = revolvers[player].remaining_shots()
        print(f"  {player}: {remaining_shots} Schuss verbleibend")
    print("-" * 50)
