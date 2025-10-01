from flask_sqlalchemy import SQLAlchemy
from .associations import films_people, species_people, people_starships, people_vehicles

db = SQLAlchemy()

class People(db.Model):
    __tablename__ = 'people'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    height = db.Column(db.String, nullable=False)
    mass = db.Column(db.String, nullable=False)
    hair_color = db.Column(db.String, nullable=False)
    skin_color = db.Column(db.String, nullable=False)
    eye_color = db.Column(db.String, nullable=False)
    birth_year = db.Column(db.String, nullable=False)
    gender = db.Column(db.String, nullable=False)
    homeworld_id = db.Column(db.Integer, db.ForeignKey('planets.id'))
    homeworld = db.relationship('Planet', backref='people')
    created = db.Column(db.String)
    edited = db.Column(db.String)
    url = db.Column(db.String)

    # Many-to-many relationships
    films = db.relationship('Film', secondary=films_people, back_populates='people')
    species = db.relationship('Species', secondary=species_people, back_populates='people')
    starships = db.relationship('Starship', secondary=people_starships, back_populates='people')
    vehicles = db.relationship('Vehicle', secondary=people_vehicles, back_populates='people')