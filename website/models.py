from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func


class Groupe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(10000))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    #invitation_code = db.Column(db.String(150))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(150))
    password = db.Column(db.String(150))
    groupe = db.relationship('Groupe')