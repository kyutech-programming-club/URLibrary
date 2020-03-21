from main import db
from flask_sqlalchemy import SQLAlchemy

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)

    def __repr__(self):
        return "<id={self.id} name={self.name}>".format(self=self)

def init():
    db.create_all()

