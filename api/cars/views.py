"""
    Module for cars routs
"""

from http import HTTPStatus

from flask import request
from flask_restx import Namespace, Resource, fields
from flask_jwt_extended import jwt_required, get_jwt_identity

from ..models.cars import Car
from ..models.users import User
from ..utils.db import db


cars_namespace = Namespace('api/avto', description="Namespace for cars")

car_model = cars_namespace.model(
    'Car', {
        # 'id': fields.Integer(description='ID'),
        'brand': fields.String(required=True, description='brand'),
        'model': fields.String(required=True, description='model'),
        'is_vintage': fields.Boolean(required=True, description='is_vintage')
    }
)


@cars_namespace.route('/cars')
class CarsGetPost(Resource):

    @cars_namespace.marshal_with(car_model)
    @cars_namespace.doc(
        description="Retrieve all cars"
    )
    @jwt_required()
    def get(self):
        """
            Retrieve all cars
        """

        cars = Car.query.all()
        return cars, HTTPStatus.OK

    @cars_namespace.expect(car_model)
    @cars_namespace.marshal_with(car_model)
    @cars_namespace.doc(
        description="Create a cars"
    )
    @jwt_required()
    def post(self):
        """
            Create new car
        """

        username = get_jwt_identity()

        current_user = User.query.filter_by(username=username).first()

        data = cars_namespace.payload

        new_car = Car(
            brand=data['brand'],
            model=data['model'],
            is_vintage=data['is_vintage']
        )

        new_car.user = current_user

        new_car.save()

        return new_car, HTTPStatus.CREATED


@cars_namespace.route('/cars/<int:car_id>')
class CarGetPutDelete(Resource):

    @cars_namespace.marshal_with(car_model)
    @cars_namespace.doc(
        description="Retrieve a car by ID",
        params={
            "car_id": "An ID for a given car"
        }
    )
    @jwt_required()
    def get(self, car_id: int):
        """
            Retrieve a car by ID
        """

        car = Car.get_by_id(car_id)

        return car, HTTPStatus.OK

    @cars_namespace.expect(car_model)
    @cars_namespace.marshal_with(car_model)
    @cars_namespace.doc(
        description="Update a car by ID",
        params={
            "car_id": "An ID for a given car"
        }
    )
    @jwt_required()
    def put(self, car_id: int):
        """
            Update a car by ID
        """

        data = cars_namespace.payload

        car = Car.get_by_id(car_id)
        car.brand = data['brand']
        car.model = data['model']
        car.is_vintage = data['is_vintage']

        db.session.commit()

        return car, HTTPStatus.OK

    @cars_namespace.marshal_with(car_model)
    @cars_namespace.doc(
        description="Delete a car by ID",
        params={
            "car_id": "An ID for a given car"
        }
    )
    @jwt_required()
    def delete(self, car_id: int):
        """
            Delete a car by ID
        """

        car = Car.get_by_id(car_id)
        car.delete()

        return car, HTTPStatus.NO_CONTENT


@cars_namespace.route('/cars/user/<int:user_id>')
class CarGetByUser(Resource):

    @cars_namespace.marshal_with(car_model)
    @cars_namespace.doc(
        description="Get car by user",
        params={
            "user_id": "An user`s ID for a given user"
        }
    )
    @jwt_required()
    def get(self, user_id: int):
        """
            Get car by user
        """

        user = User.get_by_id(user_id)

        cars = user.cars

        return cars, HTTPStatus.OK
