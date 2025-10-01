from flask_sqlalchemy import SQLAlchemy
from .associations import films_planets, films_people, films_species, films_starships, films_vehicles

db = SQLAlchemy()

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
    characters = db.relationship('People', secondary=films_people, back_populates='films')
    planets = db.relationship('Planet', secondary=films_planets, back_populates='films')
    species = db.relationship('Species', secondary=films_species, back_populates='films')
    starships = db.relationship('Starship', secondary=films_starships, back_populates='films')
    vehicles = db.relationship('Vehicle', secondary=films_vehicles, back_populates='films')