from flask_sqlalchemy import SQLAlchemy
from . import db
from .associations import films_planets

class Planet(db.Model):
    __tablename__ = 'planets'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    rotation_period = db.Column(db.String, nullable=False)
    orbital_period = db.Column(db.String, nullable=False)
    diameter = db.Column(db.String, nullable=False)
    climate = db.Column(db.String, nullable=False)
    gravity = db.Column(db.String, nullable=False)
    terrain = db.Column(db.String, nullable=False)
    surface_water = db.Column(db.String, nullable=False)
    population = db.Column(db.String, nullable=False)
    residents = db.relationship('Person', back_populates='homeworld', lazy=True)
    created = db.Column(db.String)
    edited = db.Column(db.String)
    url = db.Column(db.String)

    # Many-to-many relationships
    films = db.relationship('Film', secondary=films_planets, back_populates='planets')