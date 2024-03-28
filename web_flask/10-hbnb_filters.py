#!/usr/bin/python3
"""state liste"""
from flask import Flask
from markupsafe import escape
from flask import render_template
from models import storage
from models.amenity import Amenity
from models.state import State
from os import getenv


app = Flask(__name__)


@app.teardown_appcontext
def teardown_app_context(exception=None):
    """tear down"""
    storage.close()


@app.route('/hbnb_filters', strict_slashes=False)
def index():
    """hbnb filters"""
    if getenv("HBNB_TYPE_STORAGE") == "db":
        allstates = storage.all("State")
        allamenities = storage.all("Amenity")
    else:
        allstates = storage.all(State)
        allamenities = storage.all(Amenity)
    amenities = [amenity for amenity in allamenities.values()]
    states = [state for state in allstates.values()]
    return render_template(
            '10-hbnb_filters.html',
            states=states, amenities=amenities)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
