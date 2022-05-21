#!/usr/bin/python3
"""
Index Module
"""
from ..views import app_views
from flask import jsonify
from ....models import storage
from ....models.state import State
from ....models.amenity import Amenity
from ....models.city import City
from ....models.place import Place
from ....models.review import Review
from ....models.user import User


@app_views.route('/status', strit_slashes=False)
def status():
    """ API Status"""
    okStatus = {"status": "OK"}
    return jsonify(okStatus)


@app_views.route('stats')
def stats():
    """
        Return dict of data count
    """
    dictionnary = {"amenities": storage.count(Amenity),
                   "cities": storage.count(City),
                   "places": storage.count(Place),
                   "reviews": storage.count(Review),
                   "states": storage.count(State),
                   "users": storage.count(User)}
    return jsonify(dictionnary)
