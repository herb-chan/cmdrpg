from classes.player.Player import Player

# Load player profile
player = Player.from_profile()

player.fish()
print(player)
print(player.write_info())
print(f"You currently need: {player.exp_to_next_level()} to level up")
print(f"You currently have: {player.exp}")
player.gain_exp(10000)
print(f"You currently have: {player.exp}")
print(player.exp_needed())
print(f"You currently need: {player.exp_to_next_level()} to level up")
print(player)
print(player.write_info())

# Save player profile
player.save_profile()