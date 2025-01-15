class Formulas:
    def level_formula(self, level, wisdom):
        return (100 * (level + 1)) / wisdom * 10
    
    def gold_per_level_up_formula(self, level):
        return (100 * (level + 1))