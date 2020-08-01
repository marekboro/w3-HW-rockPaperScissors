from player import Player
from game import Game
from random import random


class Round:
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        self.choices = ["rock", "paper", "scissors"]

    def play_round(self):
        # if not self.player2.human_player:
        #     self.player2.choice = random.choice(self.choices)

        if self.player2.human_player:
            if self.player1.choice == self.player2.choice:
                return "draw"
            elif self.player1.choice == "rock":
                if self.player2.choice == "paper":
                    self.player2.won_rounds += 1

    def play_round_v_ai(self):
        self.player2.name = " Your future AI overlord"
        self.player2.choice = random.choice(self.choices)
        if self.player1.choice == self.player2.choice:
            return "draw"
        elif self.player1.choice == "rock":
            if self.player2.choice == "paper":
                self.player2.won_rounds += 1
                return f"{self.player2.name} wins"
        elif self.player1.choice == "rock":
            if self.player2.choice == "scissors":
                self.player1.won_rounds += 1
                return f"{self.player1.name} wins"

        elif self.player1.choice == "paper":
            if self.player2.choice == "scissors":
                self.player2.won_rounds += 1
                return f"{self.player2.name} wins"
        elif self.player1.choice == "paper":
            if self.player2.choice == "rock":
                self.player1.won_rounds += 1
                return f"{self.player1.name} wins"

        elif self.player1.choice == "scissors":
            if self.player2.choice == "rock":
                self.player2.won_rounds += 1
                return f"{self.player2.name} wins"
        elif self.player1.choice == "scissors":
            if self.player2.choice == "paper":
                self.player1.won_rounds += 1
                return f"{self.player1.name} wins"

