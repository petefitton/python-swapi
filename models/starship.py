from flask_sqlalchemy import SQLAlchemy
from .associations import films_starships, people_starships

db = SQLAlchemy()

class Starship(db.Model):
    __tablename__ = 'starships'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    model = db.Column(db.String, nullable=False)
    manufacturer = db.Column(db.String)
    cost_in_credits = db.Column(db.String)
    length = db.Column(db.String)
    max_atmosphering_speed = db.Column(db.String)
    crew = db.Column(db.String)
    passengers = db.Column(db.String)
    cargo_capacity = db.Column(db.String)
    consumables = db.Column(db.String)
    hyperdrive_rating = db.Column(db.String)
    MGLT = db.Column(db.String)
    starship_class = db.Column(db.String)
    created = db.Column(db.String)
    edited = db.Column(db.String)
    url = db.Column(db.String)

    # Many-to-many relationships
    films = db.relationship('Film', secondary=films_starships, back_populates='starships')
    pilots = db.relationship('People', secondary=people_starships, back_populates='starships')
