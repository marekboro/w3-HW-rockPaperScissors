import random

class Player():
    def __init__(self, name,):
        self.name = name
        self.choice = ""
        self.rounds_won = 0
        self.human_player = True

    def set_name(self, new_name):
        if len(new_name) ==0:
            pass
        else:
            self.name = new_name
    
    def installAI(self, value): 
        ai_names = ["Your futur overlord", "Toaster", "S K Y N E T"]
        if value == "yes":
            self.human_player = False
            self.name = random.choice(ai_names)
        else:
            pass
