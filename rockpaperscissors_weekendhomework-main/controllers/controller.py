from flask import render_template, request, redirect
from flask.wrappers import Request
from werkzeug.utils import redirect
from app import app
from modules import game
from modules import player

@app.route('/rps')
def index():
    return render_template('base.html')

@app.route('/rps/play')
def name_entry():
    return render_template('new_game.html')

@app.route('/rps/play/rules',methods=['GET'])
def game_rules():
    return render_template('how-to-play.html')

# @app.route('/rps/play/<choice_1>/<choice_2>')
# def play(choice_1,choice_2):
#     return f"The winner is {game.play(choice_1,choice_2)}"

# @app.route('/rps/play/<choice_1>/<choice_2>')
@app.route('/winner')
def winner():
    return render_template('winner.html')