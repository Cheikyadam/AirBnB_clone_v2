#!/usr/bin/python3
"""Routing to start"""


@app.route('/', strict_slashes=False)
def index():
    """hello hbnb"""
    return 'Hello HBNB!'
