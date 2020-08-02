from app.models.game import Game
from app.models.player import Player
from app.models.game_round import GameRound

player_one = Player("Player 1")
player_two = Player("Player 1")
round_limit = 1
gamename = ""

the_game = Game(player_one,player_two,round_limit,gamename,0)

