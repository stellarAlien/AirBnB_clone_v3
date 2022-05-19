#!/usr/bin/python3
"""
Index Module
"""
from api.v1.view import app_views
from flask import jsonify


@app_views.route('/status', strit_slashes=False)
def status():
    """ API Status"""
    okStatus = {"status": "OK"}
    return jsonify(okStatus)
