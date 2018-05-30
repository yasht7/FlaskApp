from app import db

class Character(Base):
    dec_base = declarative_base()

    name = db.Column(db.String(128), unique=True, nullable=False)
    weight = db.Column(db.Integer, nullable=False)
    speed = db.Column(db.Integer, nullable=False)
    powers = db.Column(db.String(128), nullable=False)

    def __init__(self):
        self.name = name
        self.weight = weight
        self.powers = powers
        self.speed = speed
