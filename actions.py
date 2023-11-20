from player import Player  

import random
import time
import sys



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
        if self.pl.difficulty > 5 and self.pl.difficulty <= 25:
            difficultyType = "Normal"
            
        elif self.pl.difficulty > 25 and self.pl.difficulty <= 65:
            difficultyType = "Hard"
            
        elif self.pl.difficulty > 65 and self.pl.difficulty <= 95:
            difficultyType = "Very Hard"
            
        elif self.pl.difficulty > 95 and self.pl.difficulty <= 100:
            difficultyType = "Impossible"
            
        else:
            difficultyType ="Easy"
            
        self.pl.set_difficultyType(difficultyType)    
        print("--Actual status--")
        print(f"Intelligence: {self.pl.intelligence}")
        print(f"Strong: {self.pl.strong}")
        print(f"Health: {self.pl.health}")
        print(f"Social: {self.pl.social}")
        print(f"Difficulty: {self.pl.difficultyType}")

    def give_questions(self,age):
        child_questions = {
            1: [
                [  # Questions -0
                    "Eat the toy?",
                    "Eat dust from the floor?",
                    "Eat the candy from the floor?"
                ],
                [  # Option one -1
                    "yes", "sure", "eat"
                ],
                [  # Option two -2
                    "no", "of course no"
                ],
                [  # Option three -3
                    "save", "play"
                ],
                [  # Option one data -4
                    5,  # difficulty
                    3,  # intelligence
                    3,  # strong
                    -20,  # health
                    0,  # social
                ],
                [  # Option two data -5
                    -1,  # difficulty
                    0,  # intelligence
                    0,  # strong
                    0,  # health
                    0,  # social
                ],
                [  # Option three data -6
                    0,  # difficulty
                    3,  # intelligence
                    1,  # strong
                    -5,  # health
                    1,  # social
                ]
                ],
            
            2: [
                [  # Questions -0
                    "Play with blocks?",
                    "Read a book?",
                    "Watch cartoons?"
                ],
                [  # Option one -1
                    "Yes",
                    "Sure",
                    "Play"
                ],
                [  # Option two -2
                    "No",
                    "Don't want to",
                    "Rest"
                ],
                [  # Option three -3
                    "Later",
                    "Another time",
                    "Sleep"
                ],
                [  # Option one data -4
                    -1,  # difficulty
                    2,  # intelligence
                    1,  # strong
                    0,  # health
                    1,  # social skills
                ],
                [  # Option two data -5
                    2,  # difficulty
                    -1,  # intelligence
                    1,  # strong
                    -2,  # health
                    1,  # social skills
                ],
                [  # Option three data -6
                    1,  # difficulty
                    1,  # intelligence
                    1,  # strong
                    0,  # health
                    1,  # social skills
                ]
                ],
            
            3: [
                [  # Questions -0
                    "Like soccer?",
                    "Like Futbol?",
                    "Like box?"
                ],
                [  # Option one -1
                    "Yes",
                    "Sure",
                    "Like"
                ],
                [  # Option two -2
                    "No",
                    "Don't want to",
                    "Any"
                ],
                [  # Option three -3
                    "Other sport",
                    "Later",
                    "Maybe"
                ],
                [  # Option one data -4
                    -5,  # difficulty
                    1,  # intelligence
                    5,  # strong
                    5,  # health
                    5,  # social skills
                ],
                [  # Option two data -5
                    3,  # difficulty
                    3,  # intelligence
                    -2,  # strong
                    -2,  # health
                    0,  # social skills
                ],
                [  # Option three data -6
                    -5,  # difficulty
                    1,  # intelligence
                    5,  # strong
                    5,  # health
                    5,  # social skills
                ]
                ],
            
            4: [
                [  # Questions -0
                    "Make friends?",
                    "Talk to the kids?",
                    "Lend my toys?"
                ],
                [  # Option one -1
                    "Yes",
                    "Sure",
                    "Do",
                    "Make",
                    "Talk",
                    "Lend"
                ],
                [  # Option two -2
                    "No",
                    "Don't want to",
                    "Any"
                ],
                [  # Option three -3
                    "Few",
                    "later",
                    "Maybe"
                ],
                [  # Option one data -4
                    -5,  # difficulty
                    5,  # intelligence
                    1,  # strong
                    2,  # health
                    10,  # social skills
                ],
                [  # Option two data -5
                    3,  # difficulty
                    3,  # intelligence
                    -2,  # strong
                    -2,  # health
                    0,  # social skills
                ],
                [  # Option three data -6
                    -4,  # difficulty
                    4,  # intelligence
                    1,  # strong
                    2,  # health
                    7,  # social skills
                ]
                ],
            
            5: [
                [  # Questions -0
                    "Use seat belt?",
                    "Sit on the kids seat?",
                ],
                [  # Option one -1
                    "Yes",
                    "Sit",
                    "Use",
                    "sure"
                ],
                [  # Option two -2
                    "No",
                    "Don't want to",
                    "Any"
                ],
                [  # Option three -3
                    "Short time",
                    "later",
                    "Maybe"
                ],
                [  # Option one data -4
                    10,  # difficulty
                    10,  # intelligence
                    -3,  # strong
                    -15,  # health
                    0,   # social skills
                ],
                [  # Option two data -5
                    20,  # difficulty
                    5,  # intelligence
                    -5,  # strong
                    -95,  # health
                    0,   # social skills
                ],
                [  # Option three data -6
                    15,  # difficulty
                    7,  # intelligence
                    -4,  # strong
                    -20,  # health
                    2,   # social skills
                ]
                ],
        }
        
        if age <= 5:
            return child_questions[age]
        
        
    def ask_question(self, age):
        if age <= 5:
            data = self.give_questions(age)
            question = random.choice(data[0])
            options_one = data[1]
            options_two = data[2]
            options_three = data[3]
            result_one = data[4]
            result_two = data[5]
            result_three = data[6]
            
            print(question)
            
            while True:
                select = (input("++"+self.return_player_name()+": ")).lower()
                options = [string.lower() for string in options_one]
                if select in options:
                    results = result_one
                    break
                options = [string.lower() for string in options_two]
                if select in options:
                    results = result_two
                    break
                options = [string.lower() for string in options_three]
                if select in options:
                    results = result_three
                    break
                
                time.sleep(2)
                print("**Narrator: Sorry? repeat your decision")
                
            self.make_adjustments(results, age)
            
    def make_adjustments(self, results, age):
        print(results)
        
        
        self.pl.difficulty = min(max(self.pl.difficulty + results[0], 0), 100)
        self.pl.intelligence = min(max(self.pl.intelligence + results[1], 0), 100)
        self.pl.strong = min(max(self.pl.strong + results[2], 0), 100)
        self.pl.health = min(max(self.pl.health + results[3], 0), 100)
        self.pl.social = min(max(self.pl.social + results[4], 0), 100)

        if self.pl.health == 0:
            print("__YOU DIE__")
            time.sleep(4)
            print("**God: Hey you!")
            time.sleep(2)
            print("**God: It's not a pleasure to see you again.")
            time.sleep(2)
            print("**God: I suppose that your bad decisions led to an early demise.")
            time.sleep(2)
            print("**God: We need to decide if you go to heaven or to the inferno.")
            
            average = (self.pl.intelligence + self.pl.strong + self.pl.social) / 3
            
            if age < 10:
                print("**God: Well, look at you, not even out of single digits! Heaven it is, kiddo. No surprises there.")
            elif average > 50:
                print("**God: Oh, a real brainiac, a strong athlete, and the life of the party! Off to heaven's VIP section, I suppose.")
            else:
                print("**God: Huh, tough luck! Seems like it's a downward spiral to the fiery depths. Try to bring marshmallows.")

            
            self.show_status
            sys.exit()

