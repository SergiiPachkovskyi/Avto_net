from flask import Flask
from flask_restx import Api
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
from werkzeug.exceptions import NotFound, MethodNotAllowed

from api.auth.views import auth_namespace
from api.cars.views import cars_namespace
from api.config.config import config_dict
from api.utils.db import db
from api.models.cars import Car


app = Flask(__name__)
app.config.from_object(config_dict['dev'])

api = Api(app)
api.add_namespace(cars_namespace)
api.add_namespace(auth_namespace)

jwt = JWTManager(app)

db.init_app(app)

migrate = Migrate(app, db)


@api.errorhandler(NotFound)
def not_found(error):
    return {"error": "Not found"}, 404


@api.errorhandler(MethodNotAllowed)
def method_not_allowed(error):
    return {"error": "Method not allowed"}, 405


@app.shell_context_processor
def make_shell_context():
    return {
        'db': db,
        'Car': Car
    }


if __name__ == '__main__':
    app.run()
