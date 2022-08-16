from flask import Flask
from flask_restx import Api
from flask_migrate import Migrate

from api.cars.views import cars_namespace
from api.config.config import config_dict
from api.utils.db import db
from api.models.cars import Car


app = Flask(__name__)
app.config.from_object(config_dict['dev'])
db.init_app(app)
migrate = Migrate(app, db)
api = Api(app)
api.add_namespace(cars_namespace)


@app.shell_context_processor
def make_shell_context():
    return {
        'db': db,
        'Car': Car
    }


if __name__ == '__main__':
    app.run()
