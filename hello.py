import os
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello World!'

@app.route('/foo')
def foo_bar():
    return 'Hello foo bar!'

@app.route('/api')
def json_api():
    data = {
        'foo': 'bar',
        'bla':  'blabla?'
    }
    return jsonify(data)
