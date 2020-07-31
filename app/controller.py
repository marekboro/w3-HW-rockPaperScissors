from flask import render_template
from app import app
# from app.models.player import Player
# from app.models.game import Game


string1 = '/paper/scissors'

@app.route('/')
def index():
    # return render_template('index.html', title = 'Le Rock le Paper, le scissors')
    return "Hello, World!"

@app.route('/rock/scissors')
def result():
    return "Player 1 wins by playing rock"

@app.route(string1)
def result2():
    return "Player 2 wins by playing scissors against paper"


