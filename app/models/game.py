from player import Player
import random

class Game():
    def __init__(self, player_1, player_2, max_rounds):
        self.player_1 = player_1
        self.player_2 = player_2
        self.max_rounds = max_rounds
        self.result_route = ""
        self.name = ""

    def set_name(self,name):
        self.name = name

    def set_round(self,rounds):
        self.max_rounds = rounds


   

   

        