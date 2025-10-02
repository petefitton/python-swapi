from dotenv import load_dotenv
import json
from models import db, Film, Person, Planet, Species, Starship, Vehicle
from flask import Flask
import os

load_dotenv()

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)


def get_record_from_attr(model, url_field, url):
    return model.query.filter(getattr(model, url_field) == url).first()

def get_id_from_url(model, url_field, url):
    record = get_record_from_attr(model, url_field, url)
    return record.id if record else None

def get_ids_from_urls(model, url_field, urls):
    ids = []
    for url in urls:
        record = get_id_from_url(model, url_field, url)
        if record:
            ids.append(record)
    return ids

def get_records_from_urls(model, urls):
    records = []
    for url in urls:
        record = get_record_from_attr(model, 'url', url)
        if record:
            records.append(record)
    return records


def import_films():
    with app.app_context():
        with open('seeds/films.json') as file:
            films = json.load(file)
            for f in films:
                film = Film(
                    title=f['title'],
                    episode_id=f['episode_id'],
                    opening_crawl=f['opening_crawl'],
                    director=f['director'],
                    producer=f['producer'],
                    release_date=f['release_date'],
                    # characters=get_ids_from_urls(Person, 'url', f.get('characters', [])),
                    # planets=get_ids_from_urls(Planet, 'url', f.get('planets', [])),
                    # starships=get_ids_from_urls(Starship, 'url', f.get('starships', [])),
                    # vehicles=get_ids_from_urls(Vehicle, 'url', f.get('vehicles', [])),
                    # species=get_ids_from_urls(Species, 'url', f.get('species', [])),
                    created=f['created'],
                    edited=f['edited'],
                    url=f['url'],
                )
                db.session.add(film)
            db.session.commit()

def import_people():
    with app.app_context():
        with open('seeds/people.json') as file:
            people = json.load(file)
            for p in people:
                person = Person(
                    name=p['name'],
                    height=p['height'],
                    mass=p['mass'],
                    hair_color=p['hair_color'],
                    skin_color=p['skin_color'],
                    eye_color=p['eye_color'],
                    birth_year=p['birth_year'],
                    gender=p['gender'],
                    # homeworld_id=get_id_from_url(Planet, 'url', p.get('homeworld', '')),
                    # homeworld=get_record_from_attr(Planet, 'url', p.get('homeworld', '')),
                    # films=get_ids_from_urls(Film, 'url', p.get('films', [])),
                    # species=get_ids_from_urls(Species, 'url', p.get('species', [])),
                    # starships=get_ids_from_urls(Starship, 'url', p.get('starships', [])),
                    # vehicles=get_ids_from_urls(Vehicle, 'url', p.get('vehicles', [])),
                    created=p['created'],
                    edited=p['edited'],
                    url=p['url'],
                )
                db.session.add(person)
            db.session.commit()

def import_planets():
    with app.app_context():
        with open('seeds/planets.json') as file:
            planets = json.load(file)
            for p in planets:
                planet = Planet(
                    name=p['name'],
                    rotation_period=p['rotation_period'],
                    orbital_period=p['orbital_period'],
                    diameter=p['diameter'],
                    climate=p['climate'],
                    gravity=p['gravity'],
                    terrain=p['terrain'],
                    surface_water=p['surface_water'],
                    population=p['population'],
                    # films=get_ids_from_urls(Film, 'url', p.get('films', [])),
                    # residents=get_ids_from_urls(Person, 'url', p.get('residents', [])),
                    created=p['created'],
                    edited=p['edited'],
                    url=p['url'],
                )
                db.session.add(planet)
            db.session.commit()

def import_species():
    with app.app_context():
        with open('seeds/species.json') as file:
            species = json.load(file)
            for s in species:
                species = Species(
                    name=s['name'],
                    classification=s['classification'],
                    designation=s['designation'],
                    average_height=s['average_height'],
                    skin_colors=s['skin_colors'],
                    hair_colors=s['hair_colors'],
                    eye_colors=s['eye_colors'],
                    average_lifespan=s['average_lifespan'],
                    language=s['language'],
                    # homeworld_id=get_id_from_url(Planet, 'url', s.get('homeworld', '')),
                    # films=get_ids_from_urls(Film, 'url', s.get('films', [])),
                    # people=get_ids_from_urls(Person, 'url', s.get('people', [])),
                    created=s['created'],
                    edited=s['edited'],
                    url=s['url'],
                )
                db.session.add(species)
            db.session.commit()

def import_starships():
    with app.app_context():
        with open('seeds/starships.json') as file:
            starships = json.load(file)
            for s in starships:
                starship = Starship(
                    name=s['name'],
                    model=s['model'],
                    manufacturer=s['manufacturer'],
                    cost_in_credits=s['cost_in_credits'],
                    length=s['length'],
                    max_atmosphering_speed=s['max_atmosphering_speed'],
                    crew=s['crew'],
                    passengers=s['passengers'],
                    cargo_capacity=s['cargo_capacity'],
                    consumables=s['consumables'],
                    hyperdrive_rating=s['hyperdrive_rating'],
                    MGLT=s['MGLT'],
                    starship_class=s['starship_class'],
                    # films=get_ids_from_urls(Film, 'url', s.get('films', [])),
                    # pilots=get_ids_from_urls(Person, 'url', s.get('pilots', [])),
                    created=s['created'],
                    edited=s['edited'],
                    url=s['url'],
                )
                db.session.add(starship)
            db.session.commit()

def import_vehicles():
    with app.app_context():
        with open('seeds/vehicles.json') as file:
            vehicles = json.load(file)
            for v in vehicles:
                vehicle = Vehicle(
                    name=v['name'],
                    model=v['model'],
                    manufacturer=v['manufacturer'],
                    cost_in_credits=v['cost_in_credits'],
                    length=v['length'],
                    max_atmosphering_speed=v['max_atmosphering_speed'],
                    crew=v['crew'],
                    passengers=v['passengers'],
                    cargo_capacity=v['cargo_capacity'],
                    consumables=v['consumables'],
                    vehicle_class=v['vehicle_class'],
                    # films=get_ids_from_urls(Film, 'url', v.get('films', [])),
                    # pilots=get_ids_from_urls(Person, 'url', v.get('pilots', [])),
                    created=v['created'],
                    edited=v['edited'],
                    url=v['url'],
                )
                db.session.add(vehicle)
            db.session.commit()

def import_film_relationships():
    with app.app_context():
        with open('seeds/films.json') as file:
            films = json.load(file)
            for f in films:
                film=get_record_from_attr(Film, 'url', f.get('url', ''))
                film.characters=get_records_from_urls(Person, f.get('characters', []))
                film.planets=get_records_from_urls(Planet, f.get('planets', []))
                film.starships=get_records_from_urls(Starship, f.get('starships', []))
                film.vehicles=get_records_from_urls(Vehicle, f.get('vehicles', []))
                film.species=get_records_from_urls(Species, f.get('species', []))
                db.session.commit()

def import_person_relationships():
    with app.app_context():
        with open('seeds/people.json') as file:
            people = json.load(file)
            for p in people:
                person=get_record_from_attr(Person, 'url', p.get('url', ''))
                person.homeworld_id=get_id_from_url(Planet, 'url', p.get('homeworld', ''))
                person.homeworld=get_record_from_attr(Planet, 'url', p.get('homeworld', ''))
                person.films=get_records_from_urls(Film, p.get('films', []))
                person.species=get_records_from_urls(Species, p.get('species', []))
                person.starships=get_records_from_urls(Starship, p.get('starships', []))
                person.vehicles=get_records_from_urls(Vehicle, p.get('vehicles', []))
                db.session.commit()

def import_planet_relationships():
    with app.app_context():
        with open('seeds/planets.json') as file:
            planets = json.load(file)
            for p in planets:
                planet=get_record_from_attr(Planet, 'url', p.get('url', ''))
                planet.films=get_records_from_urls(Film, p.get('films', []))
                planet.residents=get_records_from_urls(Person, p.get('residents', []))
                db.session.commit()

def import_species_relationships():
    with app.app_context():
        with open('seeds/species.json') as file:
            species = json.load(file)
            for s in species:
                spec=get_record_from_attr(Species, 'url', s.get('url', ''))
                spec.homeworld_id=get_id_from_url(Planet, 'url', s.get('homeworld', ''))
                spec.films=get_records_from_urls(Film, s.get('films', []))
                spec.people=get_records_from_urls(Person, s.get('people', []))
                db.session.commit()

def import_starship_relationships():
    with app.app_context():
        with open('seeds/starships.json') as file:
            starships = json.load(file)
            for s in starships:
                starship=get_record_from_attr(Starship, 'url', s.get('url', ''))
                starship.films=get_records_from_urls(Film, s.get('films', []))
                starship.pilots=get_records_from_urls(Person, s.get('pilots', []))
                db.session.commit()

def import_vehicle_relationships():
    with app.app_context():
        with open('seeds/vehicles.json') as file:
            vehicles = json.load(file)
            for v in vehicles:
                vehicle=get_record_from_attr(Vehicle, 'url', v.get('url', ''))
                vehicle.films=get_records_from_urls(Film, v.get('films', []))
                vehicle.pilots=get_records_from_urls(Person, v.get('pilots', []))
                db.session.commit()

if __name__ == '__main__':
    import_films()
    import_people()
    import_planets()
    import_species()
    import_starships()
    import_vehicles()
    import_film_relationships()
    import_person_relationships()
    import_planet_relationships()
    import_species_relationships()
    import_starship_relationships()
    import_vehicle_relationships()