#!/usr/bin/env python
import os
import json
import requests
from flask import Flask, render_template, jsonify, request
app = Flask(__name__, template_folder='../templates')

@app.route('/')
def index():
    months = ['January', 'February', 'March', 'April', 'May', 'June', 'July',
              'August', 'September', 'October', 'November', 'December']
    weather = {
        'January': {'min': 38, 'max': 47, 'rain': 6.14},
        'February': {'min': 38, 'max': 51, 'rain': 4.79},
        'March': {'min': 41, 'max': 56, 'rain': 4.5},
        'April': {'min': 44, 'max': 61, 'rain': 3.4},
        'May': {'min': 49, 'max': 67, 'rain': 2.55},
        'June': {'min': 53, 'max': 73, 'rain': 1.69},
        'July': {'min': 57, 'max': 80, 'rain': 0.59},
        'August': {'min': 58, 'max': 80, 'rain': 0.71},
        'September': {'min': 54, 'max': 75, 'rain': 1.54},
        'October': {'min': 48, 'max': 63, 'rain': 3.42},
        'November': {'min': 41, 'max': 52, 'rain': 6.74},
        'December': {'min': 36, 'max': 45, 'rain': 6.94}
    }
    highlight = {'min': 40, 'max': 80, 'rain': 5}    
    return render_template('index.html', city='Portland, OR', months=months,
                           weather=weather, highlight=highlight)

@app.route('/user/<name>')
def user(name):
    return '<h1>Hello, {0}!</h1>'.format(name)

###############################################################################

if __name__ == "__main__":
    app.debug = True
    port = int(os.environ.get('PORT', 5000))
    app.run('0.0.0.0', port=port)
