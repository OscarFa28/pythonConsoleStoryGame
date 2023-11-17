from player import Player  

import random


class Actions:
    def __init__(self, name):
        self.pl = Player(name)  
    
    def return_player_name(self):
        return self.pl.playerName
    
    def return_difficulty(self):
        return self.pl.difficulty
    
    def return_intelligence(self):
        return self.pl.intelligence
    
    def return_strong(self):
        return self.pl.strong
    
    def return_health(self):
        return self.pl.health
    
    def return_social(self):
        return self.pl.social
    
    def return_country(self):
        return self.pl.country
    
    def return_difficulty_type(self):
        return self.pl.difficultyType
    
    
    def set_country(self):
        easy = ["USA", "Germany", "Japan", "Canada", "Australia", "Switzerland", "Sweden"]
        normal = ["Spain", "South Korea", "France", "Italy", "Netherlands", "Belgium"]
        hard = ["Mexico", "Argentina", "Brasil", "Colombia", "El Salvador", "Russia", "India", "China"]
        veryHard = ["Peru", "Honduras", "Guatemala", "Ecuador", "Bolivia", "Vietnam", "Thailand"]
        impossible = ["Uganda", "Afghanistan", "Syria", "Yemen", "Somalia", "North Korea", "South Sudan"]
        
        difficulty = random.randint(1,100)
        
        if difficulty > 5 and difficulty <= 25:
            difficultyType = "Normal"
            country = random.choice(normal)
        elif difficulty > 25 and difficulty <= 65:
            difficultyType = "Hard"
            country = random.choice(hard)
        elif difficulty > 65 and difficulty <= 95:
            difficultyType = "Very Hard"
            country = random.choice(veryHard)
        elif difficulty > 95 and difficulty <= 100:
            difficultyType = "Impossible"
            country = random.choice(impossible)
        else:
            difficultyType ="Easy"
            country = random.choice(easy)
            
        self.pl.set_start_difficulty(difficulty)    
        self.pl.set_start_country(country)
        self.pl.set_difficultyType(difficultyType)

    
    def show_status(self):
        print("--Actual status--")
        print(f"Intelligence: {self.pl.intelligence}")
        print(f"Strong: {self.pl.strong}")
        print(f"Health: {self.pl.health}")
        print(f"Social: {self.pl.social}")
        print(f"Difficulty: {self.pl.difficulty}")
