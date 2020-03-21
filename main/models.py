from main import db
from flask_sqlalchemy import SQLAlchemy

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    favos = db.relationship("Favo", backref='user', lazy=True)

    def __repr__(self):
        return "<id={self.id} name={self.name}>".format(self=self)

class Url(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    maker = db.Column(db.Text, nullable=False)
    url = db.Column(db.Text, nullable=False)
    title = db.Column(db.Text, nullable=True)

    def __repr__(self):
        return "<id={self.id} maker={self.name}, url={self.url}, title={self.title}>".format(self=self)

class Favo(db.Model):
    
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer)
    url_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return "<id={self.id} user_id={self.user_id}, url_id={self.url_id}>".format(self=self)

def init():
    db.create_all()
