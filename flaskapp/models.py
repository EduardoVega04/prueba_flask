from flaskapp import db


class User(db.Model):
    id = db.Column(db.INTEGER, primary_key=True)
    name = db.Column(db.String(40), nullable=False)
    email = db.Column(db.String(120), nullable=False, unique=True)
    city = db.Column(db.String(30), nullable=False)
