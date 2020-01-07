from flask import Flask
import numpy as np

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello, World!'

@app.route('/roll-dice')
def dice():
    first = str(np.random.randint(1,7))
    second = str(np.random.randint(1,7))
    third = str(np.random.randint(1,7))
    return(f'{first}\n{second}\n{third}')