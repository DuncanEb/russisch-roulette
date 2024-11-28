def check_exit(input_text):
    """Beendet das Programm, falls der Benutzer 'exit' eingibt."""
    if input_text.strip().lower() == "exit":
        print("\n🎮 Spiel wurde abgebrochen!")
        exit()

def get_players():
    """
    Fragt die Spieler ab und gibt eine Liste der Spielernamen zurück.
    """
    players = []
    print("👥 Bitte geben Sie die Namen der Spieler ein (mindestens 2 Spieler).")
    print("🚪 Drücken Sie Enter ohne Eingabe, um die Eingabe zu beenden.")
    while True:
        player_name = input("➤ Spielername: ").strip()
        check_exit(player_name)
        if not player_name:
            if len(players) < 2:
                print("❌ Mindestens 2 Spieler sind erforderlich!")
                continue
            break
        players.append(player_name)
    return players

def player_shoot_logic(player, players, revolvers):
    """
    Führt die Schussaktion eines Spielers aus.
    :param player: Name des Spielers
    :param players: Liste der Spieler
    :param revolvers: Dictionary mit Revolver-Objekten pro Spieler
    :return: Dictionary mit dem Ergebnis des Schusses
    """
    result = {"lost": False}

    # Der Spieler schießt mit seinem Revolver
    if revolvers[player].shoot():
        # Spieler verliert
        result["lost"] = True
        remove_player(player, players, revolvers)

    return result

def print_revolvers_status(players, revolvers):
    """
    Zeigt den Status der Revolver für alle Spieler an.
    :param players: Liste der Spieler
    :param revolvers: Dictionary der Spieler-Revolver
    """
    print("\n🔫 Revolverstatus:")
    for player in players:
        remaining_shots = 6 - revolvers[player].current_position
        print(f"  {player}: {remaining_shots} Schuss verbleibend")
    print("-" * 50)

def remove_player(player, players, revolvers):
    """
    Entfernt einen Spieler und seinen Revolver aus den Datenstrukturen.
    """
    players.remove(player)
    del revolvers[player]
