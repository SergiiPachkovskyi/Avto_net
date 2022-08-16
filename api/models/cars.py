from ..utils.db import db


class Car(db.Model):
    """
        A class to represent a Car.
    """

    __tablename__ = 'cars'

    id = db.Column(db.Integer, primary_key=True)
    brand = db.Column(db.String(100), nullable=False)
    model = db.Column(db.String(100), nullable=False)
    is_vintage = db.Column(db.Boolean, default=False)
    owner = db.Column(db.Integer(), db.ForeignKey('users.id'))

    def save(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_by_id(cls, car_id: int):
        return cls.query.get_or_404(car_id)

    def delete(self):
        db.session.delete(self)
        db.session.commit()


