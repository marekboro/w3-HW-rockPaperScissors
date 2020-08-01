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
        if current_round>self.max_rounds:
            return current_round -1
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

    def register_choice(
        self, choice
    ):  # decide whose choice is to be registered on button press.
        can_take_values = 2 * int(self.max_rounds) - int(self.cycle)
        if can_take_values > 1:
            if self.whose_turn() == self.player_1:
                self.player_1.choice = choice
                self.cycle += 1
            elif self.whose_turn() == self.player_2:
                self.player_2.choice = choice
                self.cycle += 1
        else:
            pass

    def play_round(self):

        pass

