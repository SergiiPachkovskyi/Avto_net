import unittest
from .. import create_app, Car
from ..config.config import config_dict
from ..utils.db import db
from flask_jwt_extended import create_access_token


class CarTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app(config=config_dict['test'])
        self.appctx = self.app.app_context()

        self.appctx.push()

        self.client = self.app.test_client()

        db.create_all()

    def tearDown(self):
        db.drop_all()

        self.appctx.pop()

        self.app = None
        self.client = None

    def test_get_all_cars(self):
        token = create_access_token(identity='testuser')

        headers = {
            "Authorization": f"Bearer {token}"
        }

        response = self.client.get("/api/avto/cars", headers=headers)

        assert response.status_code == 200

        assert response.json == []

    def test_create_car(self):
        data = {
            "brand": "audi",
            "model": "xxx",
            "is_vintage": True
        }

        token = create_access_token(identity='testuser')

        headers = {
            "Authorization": f"Bearer {token}"
        }

        response = self.client.post("/api/avto/cars", json=data, headers=headers)

        assert response.status_code == 201

        cars = Car.query.all()

        assert len(cars) == 1


if __name__ == '__main__':
    unittest.main()
