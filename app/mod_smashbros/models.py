from app import db
from app.mod_auth.models import Base

class Character(Base):

    name = db.Column(db.String(128), unique=True, nullable=False)
    weight = db.Column(db.Integer, nullable=False)
    powers = db.Column(db.String(128), nullable=False)
    speed = db.Column(db.Integer, nullable=False)

    def __init__(self, name, weight, powers, speed):
        self.name = name
        self.weight = weight
        self.powers = powers
        self.speed = speed


    def __repr__(self):
        return self.name
