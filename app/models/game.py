from app.models.player import Player
import math

# from player import Player


class Game:
    def __init__(self, player_1, player_2, max_rounds, name="", cycle=0):
        self.player_1 = player_1
        self.player_2 = player_2
        self.max_rounds = max_rounds
        self.name = name
        self.cycle = cycle

    def set_name(self, new_name):
        if len(new_name) == 0:
            pass
        else:
            self.name = new_name

    def set_round(self, rounds):
        if int(rounds) == 999:
            pass
        else:
            self.max_rounds = rounds

    ## NOT USED ?
    # def set_player_1(self, Player):
    #     self.player_1 = Player

    # def set_player_2(self, Player):
    #     self.player_2 = Player
    def get_round(self):
        current_round = math.floor(1 + int(self.cycle) / 2)
        if current_round > self.max_rounds:
            return current_round - 1
        else:
            return current_round
        # return 4

    def whose_turn(
        self,
    ):  # this allow to use cycle to determine whose move it will be during the round / game cycle
        if self.cycle % 2 == 0:
            return self.player_1
        else:
            return self.player_2

    def game_can_be_played(self):
        if (2*self.max_rounds - self.cycle) >= 1:
            return True
        else:
            return False

        # ----- CURRENT vertsion of this :
        # if (self.player_1.rounds_won + self.player_1.rounds_won +1) <= self.max_rounds:
        #     return True
        # else:
        #     return False
        # ------
        # if self.cycle >= 2*self.max_rounds:
        #     return False
        # else:
        #     return True

    # decide whose choice is to be registered on button press.
    def register_choice(self, choice):
        if self.game_can_be_played():

            if self.whose_turn() == self.player_1:
                self.player_1.choice = choice
                self.cycle += 1
            elif self.whose_turn() == self.player_2:
                self.player_2.choice = choice
                self.cycle += 1

    def AImoves(self):
        if self.game_can_be_played():

            if self.player_2.human_player == False:
                self.player_2.choice = self.player_2.AImove()
                self.cycle += 1
            else:
                pass

                # if self.player_2.human_player:
                #     self.player_2.choice = choice
                #     self.cycle += 1
                # else:
                #     self.player_2.choice = self.player_2.AImove()
                #     self.cycle += 1

        # else:
        #     pass

    def p1_wins(self):
        self.player_1.rounds_won += 1
        self.player_1.choice = ""
        self.player_2.choice = ""

    def p2_wins(self):
        self.player_2.rounds_won += 1
        self.player_1.choice = ""
        self.player_2.choice = ""

        # return int(self.cycle) <= 2*int(self.max_rounds)
        # if self.cycle >= 2 * self.max_rounds:
        #     return False
        # else:
        #     return True

    def play_round(self):

        # if self.game_can_be_played():
        #     if self.player_1.choice == self.player_2.choice:
        #         pass
        #     if self.player_1.choice == "Rock" and self.player_2.choice == "Scissors":
        #         self.p1_wins()

        if self.game_can_be_played():
            if self.player_1.choice == "" or self.player_2.choice == "":
                pass
            elif self.player_1.choice == "Rock" and self.player_2.choice == "Scissors":
                self.p1_wins()
            elif self.player_1.choice == "Paper" and self.player_2.choice == "Rock":
                self.p1_wins()
            elif self.player_1.choice == "Scissors" and self.player_2.choice == "Paper":
                self.p1_wins()
            else:
                self.p2_wins()

    def announce_winner(self):
        if self.game_can_be_played() == False:
            if self.player_1.rounds_won > self.player_2.rounds_won:
                return self.player_1.name
            if self.player_2.rounds_won > self.player_1.rounds_won:
                return self.player_2.name
            if self.player_2.rounds_won == self.player_1.rounds_won:
                return "DRAW"       
        else:
            return "unknown"

        # if (self.max_rounds - 2 * self.cycle) == 1:
        #     if self.player_1.rounds_won > self.player_2.rounds_won:
        #         return self.player_1.name
        #     else:
        #         return self.player_2.name
        # else:
        #     return "still unknown"

