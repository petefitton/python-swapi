from flask_sqlalchemy import SQLAlchemy
from . import db
from .associations import films_planets, films_people, films_species, films_starships, films_vehicles

class Film(db.Model):
    __tablename__ = 'films'
    
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    episode_id = db.Column(db.Integer, nullable=False)
    opening_crawl = db.Column(db.String, nullable=False)
    director = db.Column(db.String, nullable=False)
    producer = db.Column(db.String, nullable=False)
    release_date = db.Column(db.String, nullable=False)
    created = db.Column(db.String)
    edited = db.Column(db.String)
    url = db.Column(db.String)
    
    # Many-to-many relationships
    characters = db.relationship('Person', secondary=films_people, back_populates='films')
    planets = db.relationship('Planet', secondary=films_planets, back_populates='films')
    species = db.relationship('Species', secondary=films_species, back_populates='films')
    starships = db.relationship('Starship', secondary=films_starships, back_populates='films')
    vehicles = db.relationship('Vehicle', secondary=films_vehicles, back_populates='films')

    def as_dict(self):
      characters = [self.characters[i].name for i in range(len(self.characters))]
      planets = [self.planets[i].name for i in range(len(self.planets))]
      species = [self.species[i].name for i in range(len(self.species))]
      starships = [self.starships[i].name for i in range(len(self.starships))]
      vehicles = [self.vehicles[i].name for i in range(len(self.vehicles))]

      return {
        'id': self.id,
        'title': self.title,
        'episode_id': self.episode_id,
        'opening_crawl': self.opening_crawl,
        'director': self.director,
        'producer': self.producer,
        'release_date': self.release_date,
        'created': self.created,
        'edited': self.edited,
        'url': self.url,
        'characters': characters,
        'planets': planets,
        'species': species,
        'starships': starships,
        'vehicles': vehicles,
      }