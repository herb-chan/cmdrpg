from classes.utils.Fishing import Fishing
from classes.utils.Formulas import Formulas
from classes.utils.Data import Data

class Player:
    def __init__(self, name, fishing_speed, fishing_wisdom, fishing_treasure_find, title, level, exp, gold, inventory, equipment):
        self.name = name
        self.fishing_speed = fishing_speed
        self.fishing_wisdom = fishing_wisdom
        self.fishing_treasure_find = fishing_treasure_find
        self.title = title
        self.level = level
        self.exp = exp
        self.gold = gold
        self.inventory = inventory
        self.equipment = equipment
        self.titles = Data.load_fishing_titles()
        self.applied_titles = set()

    def __str__(self):
        return f"{self.name} {self.title} ({self.level})"

    def update_title(self):
        for title_info in sorted(self.titles, key=lambda x: x['required_level'], reverse=True):
            if self.level >= title_info['required_level']:
                if title_info['title'] not in self.applied_titles:
                    self.title = title_info['title']
                    self.apply_perks(title_info['perks'])
                    self.applied_titles.add(title_info['title'])
                break

    def apply_perks(self, perks):
        for perk, value in perks.items():
            if hasattr(self, perk):
                setattr(self, perk, getattr(self, perk) + value)
    
    def level_up(self):
        self.level += 1
        self.update_title()
        print(f"{str(self)} leveled up to level {self.level}")

    def gain_exp(self, exp):
        self.exp += exp
        while self.exp >= self.exp_needed():
            self.exp -= self.exp_needed()
            self.level_up()

    def exp_needed(self):
        return Formulas().level_formula(self.level, self.fishing_wisdom)
    
    def exp_to_next_level(self):
        return self.exp_needed() - self.exp
    
    def fish(self):
        fishing = Fishing(self)
        fishing.fish()

    def write_info(self):
        info = (
            f"Name: {self.name}\n"
            f"Title: {self.title}\n"
            f"Level: {self.level}\n"
            f"Experience: {self.exp}\n"
            f"Gold: {self.gold}\n"
            f"Fishing Speed: {self.fishing_speed}\n"
            f"Fishing Wisdom: {self.fishing_wisdom}\n"
            f"Fishing Treasure Find: {self.fishing_treasure_find}\n"
            f"Inventory: {self.inventory}\n"
            f"Equipment: {self.equipment}\n"
        )
        return info