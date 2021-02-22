from datetime import datetime
from app import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(15), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    detections = db.relationship('Detections', backref='user', lazy=True)

    def __repr__(self):
        return f"User('{self.username}')"


class Detections(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    numberOfPeople = db.Column(db.Integer, primary_key=True)
    numberOfViolations = db.Column(db.Integer, primary_key=True)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"detected('{self.numberOfPeople}', '{self.numberOfViolations}')"
