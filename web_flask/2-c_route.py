#!/usr/bin/python3
"""Routing to start"""
from flask import Flask
from markupsafe import escape


app = Flask(__name__)


@app.route('/c/<text>', strict_slashes=False)
def fun(text):
    """c is fun"""
    return f"C {escape(text.replace('_', ' '))}"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
