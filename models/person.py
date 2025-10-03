from flask_sqlalchemy import SQLAlchemy
from . import db
from .associations import films_people, species_people, people_starships, people_vehicles

class Person(db.Model):
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
    created = db.Column(db.String)
    edited = db.Column(db.String)
    url = db.Column(db.String)

    # One-to-many relationship
    homeworld_id = db.Column(db.Integer, db.ForeignKey('planets.id'))
    homeworld = db.relationship('Planet', back_populates='residents')

    # Many-to-many relationships
    films = db.relationship('Film', secondary=films_people, back_populates='characters')
    species = db.relationship('Species', secondary=species_people, back_populates='people')
    starships = db.relationship('Starship', secondary=people_starships, back_populates='pilots')
    vehicles = db.relationship('Vehicle', secondary=people_vehicles, back_populates='pilots')

    def model_to_dict(obj):
      return {column.name: getattr(obj, column.name) for column in obj.__table__.columns}
    
    def as_dict(self):
      films = [self.films[i].name for i in range(len(self.films))]
      species = [self.species[i].name for i in range(len(self.species))]
      starships = [self.starships[i].name for i in range(len(self.starships))]
      vehicles = [self.vehicles[i].name for i in range(len(self.vehicles))]

      return {
        'id': self.id,
        'name': self.name,
        'height': self.height,
        'mass': self.mass,
        'hair_color': self.hair_color,
        'skin_color': self.skin_color,
        'eye_color': self.eye_color,
        'birth_year': self.birth_year,
        'gender': self.gender,
        'created': self.created,
        'edited': self.edited,
        'url': self.url,
        'homeworld': self.homeworld,
        'films': films,
        'species': species,
        'starships': starships,
        'vehicles': vehicles,
      }