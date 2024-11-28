import random

class Revolver:
    def __init__(self):
        """Initialisiert den Revolver mit 6 Kammern, eine davon tödlich."""
        self.chambers = [0, 0, 0, 0, 0, 1]
        random.shuffle(self.chambers)  # Kammern mischen
        self.current_position = 0

    def shoot(self):
        """
        Simuliert einen Schuss.
        Gibt True zurück, wenn der Schuss tödlich ist, sonst False.
        """
        shot = self.chambers[self.current_position]
        self.current_position = (self.current_position + 1) % len(self.chambers)
        return shot == 1
