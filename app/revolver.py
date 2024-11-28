import random

class Revolver:
    def __init__(self):
        """Initialisiere den Revolver mit 6 Kammern, eine davon tödlich."""
        self.chambers = [0, 0, 0, 0, 0, 1]
        random.shuffle(self.chambers)
        self.current_position = 0

    def shoot(self):
        """Simuliert das Schießen. Gibt True zurück, wenn tödlich, sonst False."""
        shot = self.chambers[self.current_position]
        self.current_position = (self.current_position + 1) % len(self.chambers)
        return shot == 1

    def remaining_shots(self):
        """Gibt die Anzahl der verbleibenden Schüsse zurück."""
        return len(self.chambers) - self.current_position
