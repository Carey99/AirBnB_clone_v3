#!/usr/bin/python3
"""Returning json from app_views routes"""
from api.v1.views import app_views
from flask import jsonify
from models import storage


@app_views.route('/status', strict_slashes=False)
def status_return():
    return jsonify({"status": "OK"})

@app_views.route('stats', strict_slashes=False)
def count():
    return jsonify({"amenities": storage.count("Amenity"),
                    "cities": storage.count("City"),
                    "places": storage.count("Place"),
                    "reviews": storage.count("Review"),
                    "states": storage.count("State"),
                    "users": storage.count("User")})
