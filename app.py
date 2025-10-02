from dotenv import load_dotenv
from flask import Flask
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

if __name__ == '__main__':
    app.run(debug=True)