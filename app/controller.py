import random
import math
from flask import render_template, redirect, request
from app import app
from app.models.player import Player
from app.models.game import Game 
from app.models.rungame import the_game
#from app.models.game_round import GameRound


# from app.models.player import Player
# from app.models.game import Game


string1 = "/paper/scissors"
choices = ["rock", "paper", "scissors"]

chosen_encounter_name = ""


@app.route("/")
def index():
    # return render_template('index.html', title = 'Le Rock, le Paper, le scissors', this_game_name = " Da Rock, Le Payper, Ze Scissorz ", encounter_name = "The End Game")
    return render_template(
        "index.html",
        title="Le Rock, le Paper, le scissors",
        this_game_name=" Da Rock, Le Payper, Ze Scissorz ",
        encounter_name=the_game.name,
        player_one_name=the_game.player_1.name,
        player_two_name=the_game.player_2.name,
        game_rounds=the_game.max_rounds,
        current_round = the_game.get_round(),
        turnOfPlayer = the_game.whose_turn().name,
        p1_rounds_won = the_game.player_1.rounds_won,
        p2_rounds_won = the_game.player_2.rounds_won,
        winner = the_game.announce_winner(),
        the_cycle = the_game.cycle +1,
        p1choice = the_game.player_1.choice,
        p2choice = the_game.player_2.choice,
        game_can_continue = the_game.game_can_be_played()

        #roundWinner = the_game.play_round().name
    )
    # return "Hello, World!"


# @app.route("/encountername", methods=["POST"])
# def update_encounter_name():
#     user_chosen_game_name = request.form["newEncounterName"]
#     return render_template(
#         "index.html",
#         title="Le Rock, le Paper, le scissors",
#         this_game_name=" Da Rock, Le Payper, Ze Scissorz ",
#         encounter_name=user_chosen_game_name,
#     )
# return f"Player 1 played rock, player 2 played {random.choice(choices)}"


# @app.route("/encountername1", methods=["POST"])
# def update_encounter_name1():
#     user_chosen_game_name = request.form["newEncounterName"]
#     return render_template(
#         "index.html",
#         title="Le Rock, le Paper, le scissors",
#         this_game_name=" Da Rock, Le Payper, Ze Scissorz ",
#         encounter_name=user_chosen_game_name,
#     )


@app.route("/setupgame", methods=["POST"])
def setupgame():

    the_game.player_1.set_name(request.form["name1"])
    the_game.player_2.set_name(request.form["name2"])

    the_game.set_round(int(request.form["round_choice"]))

    the_game.set_name(request.form["newgamename"])

    the_game.player_2.installAI(request.form["isNumber2AI"])
    the_game.cycle = 0
    return redirect("/")


@app.route("/reset", methods=["POST"])
def reset():
    the_game.player_2.set_name(" ")
    the_game.player_1.set_name(" ")
    the_game.set_round(1)
    the_game.set_name(" ")
    the_game.cycle = 0
    the_game.player_1.rounds_won = 0
    the_game.player_2.rounds_won = 0
    the_game.player_1.choice = ""
    the_game.player_2.choice = ""
    return redirect("/")


@app.route("/p1-rock", methods=["POST"])
def p1_pressed_rock():
    the_game.register_choice(request.form["rock"])
    the_game.AImoves()
    the_game.play_round()
    the_game.announce_winner()
    return redirect("/")

@app.route("/p1-paper", methods=["POST"])
def p1_pressed_paper():
    the_game.register_choice(request.form["paper"])
    the_game.AImoves()
    the_game.play_round()
    the_game.announce_winner()
    return redirect("/")


@app.route("/p1-scissors", methods=["POST"])
def p1_pressed_scissors():
    the_game.register_choice(request.form["scissors"])
    the_game.AImoves()
    the_game.play_round()
    the_game.announce_winner()
    return redirect("/")



# @app.route("/p2-rock", methods=["POST"])
# def p2_pressed_rock():
#     return "player 2 pressed rock"


# @app.route("/p2-paper", methods=["POST"])
# def p2_pressed_paper():
#     return "player 2 pressed paper"


# @app.route("/p2-scissors", methods=["POST"])
# def p2_pressed_scissors():
#     return "player 2 pressed scissors"


# def dupa():
#     new_name1 = request.form['name1']
#     new_name2 = request.form['name2']
#     new_number = request.form['round_choice']
#     #new_game_name = request.form['']

#     the_game.player_1.name = new_name1
#     the_game.player_2.name = new_name2
#     the_game.max_rounds = int(new_number)
#     the_game.name = request.form['newgamename']

#     return redirect("/")


# Weekend Homework - Rock Paper Scissors
# Create a simple flask app to allow the user to play rock, paper, scissors in their browser.

# You should be able to go to /rock/scissors and return the string "Player 1 wins by playing rock" to the page, for example.

# Write a class to represent the player. The player will have a name and their choice (rock/paper/scissors).

# Write a game class that has a function that takes in the 2 players and compares their choices and returns the winning player. If it is a draw the player should be None type.

# Change your route to use a template to display the users choices and the result.

# Extensions:
# Add a welcome page (and a route to get it) to explain the rules before the user picks their move. Add a link to this in the base template.

# Add some CSS to either/both of your pages.

# Further extension:
# Extend the game with a new page to allow the user to play against the computer.

# If they go to /play it will take the user to a form to allow them to enter their name and choose a move from a dropdown.

# Add a link to this page to the base template.

# Write a new method in the game class to generate a computer player with the name "Computer" and a random choice from rock, paper and scissors. (Look into the random.choice) library.

# Use the same game logic and results template to display the winner.
