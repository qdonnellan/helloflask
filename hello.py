import os
from flask import Flask, jsonify, render_template

app = Flask(__name__)

@app.route('/')
def hello():
    return render_template('example.html', name='FooBar')

@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return 'Post %d' % post_id

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
