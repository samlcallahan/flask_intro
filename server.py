from flask import Flask, render_template, request
import numpy as np
from model import predict

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

@app.route('/greeting')
def show_greeting_form():
    return render_template('greeting.html')

@app.route('/greeting-result', methods=["POST"])
def show_gretting_result():
    name = request.form['name']
    return render_template('greeting-result.html', name=name)

@app.route('/spam-or-ham')
def show_spam_form():
    return render_template('spam-or-ham.html')

@app.route('/spam-or-ham-result', methods=["POST"])
def show_spam_result():
    message = request.form['message']
    result = predict(message)
    return render_template('spam-or-ham-result.html', result=result)