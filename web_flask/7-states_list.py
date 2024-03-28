#!/usr/bin/python3
"""state liste"""
from flask import Flask
from markupsafe import escape
from flask import render_template
from models import storage
from models.state import State


app = Flask(__name__)


@app.teardown_appcontext
def teardown_app_context(exception=None):
    """tear down"""
    storage.close()


@app.route('/states_list', strict_slashes=False)
def index():
    """hello hbnb"""
    states = storage.all(State)
    return render_template('7-states_list.html', states=states)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
