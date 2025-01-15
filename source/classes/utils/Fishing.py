class Fishing:
    def __init__(self, player):
        self.player = player

    def fish(self):
        print(f"{self.player.name} is fishing")
        # Do fishing stuff here