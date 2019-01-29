#This is the place where the user and their medical history are created

from datetime import datetime, timedelta
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from flask import current_app
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

    authenticated = db.Column(db.Boolean, nullable=False, default=False)

    delete_time = db.Column(db.DateTime, nullable=False, default=(datetime.now() + timedelta(minutes=30)))

    personal_profile = db.relationship('Personal_Profile', backref='person')

    reminders = db.relationship('Reminders', backref="person")

    admissions = db.relationship('Admissions', backref="person")
    illnesses = db.relationship('Illnesses', backref="person")
    surgeries = db.relationship('Surgeries', backref="person")
    blood_transfusions = db.relationship('Blood_Transfusions', backref='person')
    allergies = db.relationship('Allergies', backref="person")
    vaccinations = db.relationship('Vaccinations', backref="person")


    #For password reset
    def get_reset_token(self, expires_sec=86400): #1800 sec is 30 mins
        s = Serializer(current_app.config['SECRET_KEY'], expires_sec)
        return s.dumps({'user_id':self.id}).decode('utf-8')

    @staticmethod #to inform python there's no self argument and only token is accepted as argument
    def verify_reset_token(token):
        s = Serializer(current_app.config['SECRET_KEY'])
        try:
            user_id = s.loads(token)['user_id']
        except:
            return None
        return User.query.get(user_id)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"


class Personal_Profile(db.Model):

    id = db.Column(db.Integer, primary_key=True)

    full_name = db.Column(db.String(60), nullable=True)
    nric = db.Column(db.String(9), unique=True, nullable=True)
    birthday = db.Column(db.DateTime, nullable=True)
    sex = db.Column(db.String(20), nullable=True)
    address = db.Column(db.String(100), nullable=True)

    age = db.Column(db.Integer, nullable=True)
    height = db.Column(db.Float, nullable=True)
    weight = db.Column(db.Float, nullable=True)
    heart_rate = db.Column(db.Integer, nullable=True)
    bmi = db.Column(db.Integer, nullable=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"Personal_Profile('{self.age}', '{self.sex}', '{self.address}', '{self.full_name}', '{self.nric}')"

class Reminders(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    reminder = db.Column(db.String, nullable=False)
    date = db.Column(db.DateTime, nullable=False, default=datetime.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"Previous_Admissions('{self.reminder}','{self.date}', '{self.user_id}', '{self.id       }')"



# region Past Medical History
class Admissions(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    reason = db.Column(db.String(100), nullable=False)
    place = db.Column(db.String(100), nullable=True)
    date = db.Column(db.DateTime, nullable=True, default=datetime.now())
    comments = db.Column(db.String(100), nullable=True)

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"Previous_Admissions('{self.place}', '{self.date}', '{self.comments}')"

class Surgeries(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    surgery_type = db.Column(db.String(100), nullable=True)

    date = db.Column(db.DateTime, nullable=True, default=datetime.now)

    place = db.Column(db.String(100), nullable=True)

    comments = db.Column(db.String(100), nullable=True)

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'),nullable=False)

    def __repr__(self):
        return f"Previous_Admissions('{self.surgery_type}','{self.place}', '{self.date}', '{self.comments}')"

class Blood_Transfusions(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    blood_type = db.Column(db.String(100), nullable=True)

    date = db.Column(db.DateTime, nullable=True, default=datetime.now)

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

class Vaccinations(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    vaccine = db.Column(db.String(100), nullable=False)
    date = db.Column(db.DateTime, nullable=True)

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

class Illnesses(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    illness = db.Column(db.String(100), nullable=False)
    date = db.Column(db.DateTime, nullable=True)

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
# endregion




# region Teammates' database model

#review
class Post_review(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.now())

    def __repr__(self):
        return f"Post_review('{self.content}', '{self.date_posted}')"


#feedback
class Content(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    subject = db.Column(db.String(50), nullable=False)
    content = db.Column(db.Text, nullable=False)


    def __repr__(self):
        return f"Content('{self.subject}')"


class Symptom(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    symptom_answer = db.Column(db.String(60), nullable=False)
    symptom_treatment = db.Column(db.String(250), nullable=False)
    symptom_password = db.Column(db.String(60), nullable=False, unique=True)

    def __repr__(self):
        return f"Symptom('{self.symptom_answer}', '{self.symptom_treatment}', '{self.symptom_password}')"


class Symptom_qa(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    question = db.Column(db.String(250), nullable=False)
    answer_1 = db.Column(db.String(250), nullable=False)
    answer_2 = db.Column(db.String(250), nullable=False)
    answer_3 = db.Column(db.String(250), nullable=False)
    answer_4 = db.Column(db.String(250), nullable=False)
    answer_5 = db.Column(db.String(250), nullable=False)

    def __repr__(self):
        return f"Symptom_qa('{self.question}', '{self.answer_1}', '{self.answer_2}', '{self.answer_3}'" \
f", '{self.answer_4}', '{self.answer_5}')"

class Trivia(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    image = db.Column(db.String(50), nullable=False)
    type = db.Column(db.String(20), nullable=True)

# endregion


