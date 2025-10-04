from flask_sqlalchemy import SQLAlchemy
from . import db
from .associations import films_species, species_people
from .tools.model_to_dict import model_to_dict

class Species(db.Model):
    __tablename__ = 'species'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    classification = db.Column(db.String, nullable=False)
    designation = db.Column(db.String, nullable=False)
    average_height = db.Column(db.String, nullable=False)
    skin_colors = db.Column(db.String, nullable=False)
    hair_colors = db.Column(db.String, nullable=False)
    eye_colors = db.Column(db.String, nullable=False)
    average_lifespan = db.Column(db.String, nullable=False)
    language = db.Column(db.String, nullable=False)
    created = db.Column(db.String)
    edited = db.Column(db.String)
    url = db.Column(db.String)

    # One-to-many relationship (with no back_populates connection)
    homeworld_id = db.Column(db.Integer, db.ForeignKey('planets.id'))

    # Many-to-many relationships
    films = db.relationship('Film', secondary=films_species, back_populates='species')
    people = db.relationship('Person', secondary=species_people, back_populates='species')

    def model_to_dict(self):
        return model_to_dict(self)