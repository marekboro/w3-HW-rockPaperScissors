from player import Player
import random

class Game():
    def __init__(self, player_1, player_2):
        self.player_1 = player_1
        self.player_2 = player_2
        self.result_route = ""

    def player_2_choice(self):
        choices = ["rock","paper","scissors"]
        self.player_2.choice = random.choice(choices)

    def play_round(self):
        choice_1 = self.player_1.choice
        choice_2 = self.player_2.choice


        if choice_1 == choice_2:
            return None
        elif choice_1 == "rock" and choice_2 == "scissors":
            self.player_1.victory = True
            return self.player_1
        elif choice_1 == "rock" and choice_2 == "paper":
            self.player_2.victory = True
            return self.player_2

        elif choice_1 == "paper" and choice_2 == "rock":
            self.player_1.victory = True
            return self.player_1
        elif choice_1 == "paper" and choice_2 == "scissors":
            self.player_2.victory = True
            return self.player_2

        elif choice_1 == "scissors" and choice_2 == "paper":
            self.player_1.victory = True
            return self.player_1
        elif choice_1 == "scissors" and choice_2 == "rock":
            self.player_2.victory = True
            return self.player_2

   

        