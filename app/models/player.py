import random
#from game import Game
#from app.models.rungame import the_game
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
            #the_game.player_2.set_name("Squishy Human")
        else:
            pass
    
    def AImove(self):
        options = ["Rock","Paper","Scissors"]
        return random.choice(options)
    
    def AIanihilateHuman(self,anotherPlayer):
        if anotherPlayer.choice == "Rock":
            return "Paper"
        if anotherPlayer.choice == "Paper":
            return "Scissors"
        if anotherPlayer.choice == "Scissors":
            return "Rock"