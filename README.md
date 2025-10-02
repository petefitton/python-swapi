# Flask + SQLAlchemy + Postgres SWAPI

## Setup

1. Install dependencies (consider using venv):
   ```bash
   pip install -r requirements.txt
   ```
2. Set up your PostgreSQL database and update the `DATABASE_URL` environment variable in your shell or `.env` file:
   ```bash
   DATABASE_URL=postgresql://user:password@localhost:5432/dbname
   ```
3. Initialize the database tables:
   ```python
   flask db init
   flask db migrate
   flask db upgrade
   ```
4. Run the Flask app:
   ```bash
   python app.py
   ```
