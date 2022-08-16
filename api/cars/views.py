from http import HTTPStatus

from flask import request
from flask_restx import Namespace, Resource, fields

from ..models.cars import Car
from ..utils.db import db

cars_namespace = Namespace('/', description="Namespace for cars")

car_model = cars_namespace.model(
    'Car', {
        'id': fields.Integer(description='ID'),
        'brand': fields.String(required=True, description='brand'),
        'model': fields.String(required=True, description='model'),
        'is_vintage': fields.Boolean(required=True, description='is_vintage')
    }
)


@cars_namespace.route('/api/cars')
class CarsGetPost(Resource):
    @cars_namespace.marshal_with(car_model)
    def get(self):
        """
            Get all cars
        """

        cars = Car.query.order_by(Car.brand).all()
        return cars, HTTPStatus.OK

    @cars_namespace.marshal_with(car_model)
    def post(self):
        """
            Create new car
        """

        data = request.get_json()
        print(data)
        new_car = Car(
            brand=data.get('brand'),
            model=data.get('model'),
            is_vintage=data.get('is_vintage')
        )

        new_car.save()

        return new_car, HTTPStatus.CREATED


@cars_namespace.route('/api/cars/<int:car_id>')
class CarGetPutDelete(Resource):
    @cars_namespace.marshal_with(car_model)
    def get(self, car_id):
        """
            Get car by car_id
        """

        car = Car.get_by_id(car_id)

        return car, HTTPStatus.OK

    def put(self, car_id):
        """
            Update by car_id
        """

        data = cars_namespace.payload

        car = Car.get_by_id(car_id)
        car.brand = data['brand']
        car.model = data['model']
        car.is_vintage = data['is_vintage']

        db.session.commit()

        return car, HTTPStatus.OK

    @cars_namespace.marshal_with(car_model)
    def delete(self, car_id):
        """
            Delete by car_id
        """

        car = Car.get_by_id(car_id)
        car.delete()

        return car, HTTPStatus.NO_CONTENT
