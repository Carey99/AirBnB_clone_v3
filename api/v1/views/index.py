#!/usr/bin/python3
"""Returning json from app_views routes"""
from api.v1.views import app_views
from flask import jsonify
from models import storage


@app_views.route('/status', strict_slashes=False)
def status_return():
    return jsonify({"status": "OK"})
