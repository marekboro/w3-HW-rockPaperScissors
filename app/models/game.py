from app.models.player import Player
#from player import Player


class Game():
    def __init__(self, player_1, player_2, max_rounds, name =""):
        self.player_1 = player_1
        self.player_2 = player_2
        self.max_rounds = max_rounds
        self.name = name

    def set_name(self,new_name):
        if len(new_name) ==0:
            pass    
        else:
            self.name = new_name

    def set_round(self,rounds):
        if int(rounds) == 999 :
           pass
        else:
            self.max_rounds = rounds

    def set_player_1(self, Player):
        self.player_1 = Player

    def set_player_2(self, Player):
        self.player_2 = Player


    def play_round(self):
        pass

    
    


   

   

        