from flask_sqlalchemy import SQLAlchemy
from .associations import films_species, species_people

db = SQLAlchemy()

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
  homeworld_id = db.Column(db.Integer, db.ForeignKey('planets.id'))
  homeworld = db.relationship('Planet', backref='species')
  created = db.Column(db.String)
  edited = db.Column(db.String)
  url = db.Column(db.String)

  # Many-to-many relationships
  films = db.relationship('Film', secondary=films_species, back_populates='species')
  people = db.relationship('People', secondary=species_people, back_populates='species')