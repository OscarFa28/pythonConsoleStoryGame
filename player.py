class Player:
    
    def __init__(self, name):
        self.playerName = name
        self.difficulty = 0
        self.intelligence = 0
        self.strong = 0
        self.health = 100
        self.social = 0
        self.country = ""
        self.difficultyType = ""
        
    def set_start_difficulty(self, difficulty):
        self.difficulty = difficulty    
        
    def set_start_country(self, country):
        self.country = country
        
    def set_difficultyType(self, difficultyType):
        self.difficultyType = difficultyType