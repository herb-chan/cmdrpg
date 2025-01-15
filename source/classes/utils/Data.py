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