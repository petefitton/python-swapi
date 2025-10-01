from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

from .film import Film
from .people import People
from .planet import Planet
from .species import Species
from .starship import Starship
from .vehicle import Vehicle