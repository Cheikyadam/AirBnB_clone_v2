#!/usr/bin/python3
"""Routing to start"""
from flask import Flask
from markupsafe import escape


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    """hello hbnb"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def index2():
    """hello hbnb"""
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def fun(text):
    """c is fun"""
    return f"C {escape(text.replace('_', ' '))}"


@app.route('/python/', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def cool(text=None):
    """Python is cool"""
    if text is None:
        text = "is_cool"
    return f"Python {escape(text.replace('_', ' '))}"


@app.route('/number/<int:n>', strict_slashes=False)
def isNumber(n):
    """c is fun"""
    return f"{escape(n)} is a number"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
