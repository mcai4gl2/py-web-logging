from flask import Blueprint, Flask, jsonify, current_app
from flask_swagger import swagger


def create_app():
    app = Flask(__name__)

    from .api import api as api_blueprint
    app.register_blueprint(api_blueprint, url_prefix='/api/v1.0')

    return app
