
from flask import Flask
from flask_wtf import FlaskForm
from wtforms import StringField , SubmitField,TextAreaField
from wtforms.validators import DataRequired, Length
from flask_sqlalchemy import SQLAlchemy

app = Flask (__name__)
app.config["SQLALCHEMY_DATABASE_URI"]='sqlite:///site.db'
db= SQLAlchemy(app)

class Content (db.Model):
    id = db.Column(db.Integer, primary_key=True)
    subject = db.Column(db.String(50), nullable=False)
    content = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f"Content('{self.subject}')"



class Feedback(FlaskForm):
    subject = StringField("Subject", validators=[DataRequired()])

    content = TextAreaField("Content", validators=[DataRequired(),Length(max=255)])

    submit = SubmitField("Submit")





