import json
import os

class Data:
    @staticmethod
    def load_json(file_path):
        with open(file_path, 'r') as file:
            return json.load(file)
        
    @staticmethod
    def load_fishing_titles():
        base_path = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(base_path, '..', '..', 'data', 'fishing_titles.json')
        return Data.load_json(file_path)

    @staticmethod
    def load_profile():
        base_path = os.path.dirname(os.path.abspath(__file__))
        player_file_path = os.path.join(base_path, '..', '..', 'data', 'player.json')
        starting_file_path = os.path.join(base_path, '..', '..', 'data', 'starting_player.json')
        
        if os.path.exists(player_file_path):
            return Data.load_json(player_file_path)
        else:
            return Data.load_json(starting_file_path)

    @staticmethod
    def save_profile(player_data):
        base_path = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(base_path, '..', '..', 'data', 'player.json')
        with open(file_path, 'w') as file:
            json.dump(player_data, file, indent=4)