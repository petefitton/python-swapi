from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

species_people = db.Table(
    'species_people',
    db.Column('species_id', db.Integer, db.ForeignKey('species.id')),
    db.Column('people_id', db.Integer, db.ForeignKey('people.id'))
)

films_people = db.Table(
    'films_people',
    db.Column('film_id', db.Integer, db.ForeignKey('films.id')),
    db.Column('people_id', db.Integer, db.ForeignKey('people.id'))
)

films_planets = db.Table(
    'films_planets',
    db.Column('film_id', db.Integer, db.ForeignKey('films.id')),
    db.Column('planet_id', db.Integer, db.ForeignKey('planets.id'))
)

films_starships = db.Table(
    'films_starships',
    db.Column('film_id', db.Integer, db.ForeignKey('films.id')),
    db.Column('starship_id', db.Integer, db.ForeignKey('starships.id'))
)

films_vehicles = db.Table(
    'films_vehicles',
    db.Column('film_id', db.Integer, db.ForeignKey('films.id')),
    db.Column('vehicle_id', db.Integer, db.ForeignKey('vehicles.id'))
)

films_species = db.Table(
    'films_species',
    db.Column('film_id', db.Integer, db.ForeignKey('films.id')),
    db.Column('species_id', db.Integer, db.ForeignKey('species.id'))
)

people_vehicles = db.Table(
    'people_vehicles',
    db.Column('people_id', db.Integer, db.ForeignKey('people.id')),
    db.Column('vehicle_id', db.Integer, db.ForeignKey('vehicles.id'))
)

people_starships = db.Table(
    'people_starships',
    db.Column('people_id', db.Integer, db.ForeignKey('people.id')),
    db.Column('starship_id', db.Integer, db.ForeignKey('starships.id'))
)

films_planets = db.Table(
    'films_planets',
    db.Column('film_id', db.Integer, db.ForeignKey('films.id')),
    db.Column('planet_id', db.Integer, db.ForeignKey('planets.id'))
)