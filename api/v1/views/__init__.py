#!/usr/bin/python3
""" API Blueprint"""
from flask import Blueprint
app_views = Blueprint('app_views', __name__, url_prefix='/api/v1')


from api.v1.views.index import *  # noqa: E402, E261

"""import flask app  views"""
from api.v1.views.states import *
from api.v1.vies.cities import *
