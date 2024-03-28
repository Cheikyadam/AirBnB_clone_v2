#!/usr/bin/python3
"""state liste"""
from flask import Flask
from markupsafe import escape
from flask import render_template
from models import storage
from models.state import State
from models.city import City
from os import getenv


app = Flask(__name__)


@app.teardown_appcontext
def teardown_app_context(exception=None):
    """tear down"""
    storage.close()


@app.route('/states', strict_slashes=False)
def index():
    """cities by state"""
    if getenv("HBNB_TYPE_STORAGE") == "db":
        allstates = storage.all("State")
    else:
        allstates = storage.all(State)
    states = [state for state in allstates.values()]
    return render_template('7-states_list.html', states=states)


@app.route('/states/<id>', strict_slashes=False)
def cities(id):
    """cities by state"""
    if getenv("HBNB_TYPE_STORAGE") == "db":
        allstates = storage.all("State")
    else:
        allstates = storage.all(State)
    realId = "State." + id
    try:
        mystate = allstates[realId]
    except KeyError:
        mystate = None
    return render_template('9-states.html', state=mystate)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
