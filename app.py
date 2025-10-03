from dotenv import load_dotenv
from flask import Flask, jsonify
from models import db, Film, Person, Planet, Species, Starship, Vehicle
from flask_migrate import Migrate
import os

load_dotenv()

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
migrate = Migrate(app, db)

@app.route('/')
def index():
    return 'Flask API is running!'

@app.route('/films')
def get_all_films():
    all_films = Film.query.all()
    if len(all_films) > 0:
        results = [film.model_to_dict() for film in all_films]
    else:
        results = []
    return jsonify(results)



if __name__ == '__main__':
    app.run(debug=True)