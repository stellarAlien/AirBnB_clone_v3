#!/usr/bin/python3
"""
main module
"""
from os import getenv
from flask import Flask, jsonify, make_response
from models import storage
from api.v1.views import app_views
app = Flask(__name__)

app.register_blueprint(app_views)


@app.teardown_appcontext
def teardown_appcontext():
    """ Teardown app context function"""
    storage.close()


@app.errorhandler(404)
def not_found_error():
    """return error in json"""
    return make_response(jsonify({"error": "Not found"}), 404)


if __name__ == "__main__":
    host = getenv('HBNB_API_HOST', '0.0.0.0')
    port = getenv('HBNB_API_PORT', '5000')
    app.run(host=host, port=port, threaded=True)
