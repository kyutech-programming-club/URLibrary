import os

SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or "sqlite:///main.db"
SQLALCHEMY_TRACK_MODIFICATIONS = True
SECRET_KEY = os.environ["SECRET_KEY"]
