from flask import render_template, redirect
from app import app
import random
# from app.models.player import Player
# from app.models.game import Game


string1 = '/paper/scissors'

choices = ['rock','paper','scissors']
# random_value = random.choice(['rock','paper','scissors'])



@app.route('/')
def index():
    return render_template('index.html', title = 'Le Rock, le Paper, le scissors', game_name = " Da Rock, Le Payper, Ze Scissorz ")
    # return "Hello, World!"

@app.route('/rock/scissors', methods = ['POST'])
def result():
    #return redirect("/")
    return "Player 1 wins by playing rock"

@app.route(string1, methods = ['POST'])
def result2():
    return "Player 2 wins by playing scissors against paper"


# string2 = f"/{name}/{random_value}"

@app.route('/rock', methods = ['POST'])
def result3():
    return f"Player 1 played rock, player 2 played {random.choice(choices)}"
