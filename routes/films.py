from flask import jsonify, Blueprint
from models import Film

films_bp = Blueprint('films', __name__, url_prefix='/films')

@films_bp.route('/')
def get_all_films():
    all_films = Film.query.all()
    if len(all_films) > 0:
        results = [film.model_to_dict() for film in all_films]
    else:
        results = []
    return jsonify(results)

@films_bp.route('/<int:film_id>')
def get_one_film(film_id):
    film = Film.query.filter_by(id=film_id).first()
    if not film:
        return jsonify({'error_message': 'Film not found'}), 404
    return jsonify(film.model_to_dict())