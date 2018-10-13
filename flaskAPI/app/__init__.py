from flask import Flask, Blueprint
from flask_restful import Api
from instance.config import app_config
from app.api.v1.views import Orders

blue= Blueprint('api', __name__)
api = Api(blue)
def create_app(config_name):
    app =Flask(__name__, instance_relative_config=True)
    app.config.from_object(app_config[config_name])
    app.config.from_pyfile('config.py')

    app.register_blueprint(blue, url_prefix='api/v1')
    app.add_resource(Order, '/')
    return app