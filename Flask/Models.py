#This is the place where the user and their medical history are created

from datetime import datetime
from Flask import db, login_manager
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)

    username = db.Column(db.String(20), unique=True, nullable=False)

    email = db.Column(db.String(120), unique=True, nullable=False)

    password = db.Column(db.String(60), nullable=False)

    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')

    # past_medical_history = db.relationship('Past_Medical_History', backref='person', lazy=True, uselist=False)

    personal_profile = db.relationship('Personal_Profile', backref='person')

    admissions = db.relationship('Admissions', backref="person")
    surgeries = db.relationship('Surgeries', backref="person")
    blood_transfusions = db.relationship('Blood_Transfusions', backref='person')
    allergies = db.relationship('Allergies', backref="person")
    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"


class Personal_Profile(db.Model):

    id = db.Column(db.Integer, primary_key=True)

    full_name = db.Column(db.String(60), nullable=True)
    nric = db.Column(db.String(9), unique=True, nullable=True)
    birthday = db.Column(db.DateTime, nullable=True)
    sex = db.Column(db.String(20), nullable=True)
    address = db.Column(db.String(100), nullable=True)

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"Personal_Profile('{self.age}', '{self.sex}', '{self.address}', '{self.full_name}', '{self.nric}')"

class Admissions(db.Model):

    id = db.Column(db.Integer, primary_key=True)

    place = db.Column(db.String(100), nullable=True)
    date = db.Column(db.DateTime, nullable=True, default=datetime.utcnow())
    comments = db.Column(db.String(100), nullable=True)

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"Previous_Admissions('{self.place}', '{self.date}', '{self.comments}')"


class Surgeries(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    surgery_type = db.Column(db.String(100), nullable=True)

    date = db.Column(db.DateTime, nullable=True, default=datetime.utcnow)

    place = db.Column(db.String(100), nullable=True)

    comments = db.Column(db.String(100), nullable=True)

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'),nullable=False)

    def __repr__(self):
        return f"Previous_Admissions('{self.surgery_type}','{self.place}', '{self.date}', '{self.comments}')"

class Blood_Transfusions(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    blood_type = db.Column(db.String(100), nullable=True)

    date = db.Column(db.DateTime, nullable=True, default=datetime.utcnow)

    place = db.Column(db.String(100), nullable=True)

    comments = db.Column(db.String(100), nullable=True)

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"Previous_Admissions('{self.blood_type}','{self.place}', '{self.date}', '{self.comments}')"

class Allergies(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    allergy = db.Column(db.String(100), nullable=True)

    date = db.Column(db.DateTime, nullable=True)

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"Previous_Admissions('{self.allergy}','{self.date_diagnosed}')"

#review
# class Post_review(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     content = db.Column(db.String(), nullable=False)
#     date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow())
#
#     def __repr__(self):
#         return f"Post_review('{self.content}', '{self.date_posted}')"
#
#
# #feedback
# class Content(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     subject = db.Column(db.String(50), nullable=False)
#     content = db.Column(db.Text, nullable=False)
#
#
#     def __repr__(self):
#         return f"Content('{self.subject}')"