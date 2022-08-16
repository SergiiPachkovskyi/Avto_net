from ..utils.db import db


class Car(db.Model):
    __tablename__ = 'cars'

    id = db.Column(db.Integer, primary_key=True)
    brand = db.Column(db.String(100), nullable=False)
    model = db.Column(db.String(100), nullable=False)
    is_vintage = db.Column(db.Boolean, default=False)

    def __init__(self, brand, model, is_vintage):
        self.brand = brand
        self.model = model
        self.is_vintage = is_vintage

    def __repr__(self):
        return f'<User {self.id} {self.brand} {self.model}>'

    def save(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_by_id(cls, car_id):
        return cls.query.get_or_404(car_id)

    def delete(self):
        db.session.delete(self)
        db.session.commit()


