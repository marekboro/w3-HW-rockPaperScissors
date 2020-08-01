from app.models.game import Game
from app.models.player import Player
from app.models.game_round import GameRound

player_one = Player("Batman")
player_two = Player("Joker")
round_limit = 10
gamename = "somethingsdsds "

the_game = Game(player_one,player_two,round_limit,gamename)

