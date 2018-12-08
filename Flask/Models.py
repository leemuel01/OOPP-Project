from datetime import datetime
from Flask import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    password = db.Column(db.String(60), nullable=False)


    full_name = db.Column(db.String(60), nullable=False)
    nric = db.Column(db.String(9), unique=True, nullable=False)

    history = db.relationship('History', backref='person', lazy=True)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}', {self.full_name}, {self.nric})"

class History(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    symptom = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"History('{self.symptom}', '{self.date_posted}'')"