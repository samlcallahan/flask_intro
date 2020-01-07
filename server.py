from flask import Flask, render_template
import numpy as np

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/roll-dice/<n_dice>')
def dice(n_dice):
    rolls = []
    for _ in range(int(n_dice)):
        rolls.append(str(np.random.randint(1,7)))
    return render_template('dice.html', n_dice=n_dice, rolls=rolls)