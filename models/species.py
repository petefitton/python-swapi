from flask_sqlalchemy import SQLAlchemy
from . import db
from .associations import films_species, species_people

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
    
    def as_dict(self):
      films = [self.films[i].name for i in range(len(self.films))]
      people = [self.people[i].name for i in range(len(self.people))]

      return {
        'id': self.id,
        'name': self.name,
        'classification': self.classification,
        'designation': self.designation,
        'average_height': self.average_height,
        'skin_colors': self.skin_colors,
        'hair_colors': self.hair_colors,
        'eye_colors': self.eye_colors,
        'average_lifespan': self.average_lifespan,
        'language': self.language,
        'created': self.created,
        'edited': self.edited,
        'url': self.url,
        'homeworld_id': self.homeworld_id,
        'films': films,
        'people': people,
      }