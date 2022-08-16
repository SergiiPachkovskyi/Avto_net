# from flask import Flask
# from flask_restx import Api
# from flask_migrate import Migrate
#
# from .cars.views import cars_namespace
# from .config.config import config_dict
# from .utils import db
# from .models.cars import Car
#
#
# def create_app(config=config_dict['dev']):
#     app = Flask(__name__)
#     app.config.from_object(config)
#     db.init_app(app)
#     migrate = Migrate(app, db)
#     api = Api(app)
#     api.add_namespace(cars_namespace)
#
#     @app.shell_context_processor
#     def make_shell_context():
#         return {
#             'db': db,
#             'Car': Car
#         }
#
#     return app
