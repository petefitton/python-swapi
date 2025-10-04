from flask import jsonify, Blueprint, request
from models import db, Film

films_bp = Blueprint('films', __name__, url_prefix='/films')

@films_bp.route('/', methods=['GET'])
def get_all_films():
    all_films = Film.query.all()
    if len(all_films) > 0:
        results = [film.model_to_dict() for film in all_films]
    else:
        results = []
    return jsonify(results)

@films_bp.route('/<int:film_id>', methods=['GET'])
def get_one_film(film_id):
    film = Film.query.filter_by(id=film_id).first()
    if not film:
        return jsonify({'error_message': 'Film not found'}), 404
    return jsonify(film.model_to_dict())

@films_bp.route('/', methods=['POST'])
def create_film():
    film = Film(
        title=request.form['title'],
        episode_id=request.form['episode_id'],
        opening_crawl=request.form['opening_crawl'],
        director=request.form['director'],
        producer=request.form['producer'],
        release_date=request.form['release_date'],
        url=request.form['url'],
        # characters=request.form['characters'] or None,
        # planets=request.form['planets'] or None,
        # starships=request.form['starships'] or None,
        # vehicles=request.form['vehicles'] or None,
        # species=request.form['species'] or None,
    )
    db.session.add(film)
    db.session.commit()
    # return jsonify(Film.query.filter_by(id=film.id).first().model_to_dict())
    return jsonify(film.model_to_dict())

@films_bp.route('/<int:film_id>', methods=['PUT'])
def update_film(film_id):
    film = Film.query.filter_by(id=film_id).first()
    if film:
        film.title=request.form['title'] or film.title
        film.episode_id=request.form['episode_id'] or film.episode_id
        film.opening_crawl=request.form['opening_crawl'] or film.opening_crawl
        film.director=request.form['director'] or film.director
        film.producer=request.form['producer'] or film.producer
        film.release_date=request.form['release_date'] or film.release_date
        film.created=request.form['created'] or film.created
        film.edited=request.form['edited'] or film.edited
        film.url=request.form['url'] or film.url
        film.characters=request.form['characters'] or film.characters
        film.planets=request.form['planets'] or film.planets
        film.starships=request.form['starships'] or film.starships
        film.vehicles=request.form['vehicles'] or film.vehicles
        film.species=request.form['species'] or film.species
        return jsonify(film.model_to_dict())
    else:
        return jsonify({'error_message': 'Film not found'}), 404

@films_bp.route('/<int:film_id>', methods=['DELETE'])
def delete_film(film_id):
    film = Film.query.filter_by(id=film_id).first()
    if film:
        db.session.delete(film)
        db.session.commit()
        return jsonify(film.model_to_dict())
    else:
        return jsonify({'error_message': 'Film not found'}), 404