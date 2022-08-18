# from api import create_app
# from api.config.config import config_dict

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


def create_app(config=config_dict['dev']):
    app = Flask(__name__)
    app.config.from_object(config)

    authorizations = {
        "Bearer Auth": {
            'type': 'apiKey',
            'in': 'header',
            'name': 'Authorization',
            'description': 'Add a JWT with ** Bearer &lt;JWT&gt; to authorize'
        }
    }

    api = Api(
        app,
        title='Avto.net API',
        description="A REST API for a Avto.net",
        authorizations=authorizations,
        security="Bearer Auth"
    )
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

    return app


if __name__ == '__main__':
    app = create_app(config_dict['prod'])
    app.run()
