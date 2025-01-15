from classes.player.Player import Player

player = Player("John", 10, 1, 10, "Fisherman", 1, 0, 0, [], [])
player.fish()
print(player)
print(player.write_info())
print(f"You currently need: {player.exp_to_next_level()} to level up")
print(f"You currently have: {player.exp}")
player.gain_exp(player.exp_to_next_level() * 100 - 1100)
print(f"You currently have: {player.exp}")
print(player.exp_needed())
print(f"You currently need: {player.exp_to_next_level()} to level up")
print(player)
print(player.write_info())