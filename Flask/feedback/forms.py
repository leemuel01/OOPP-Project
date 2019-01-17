from flask_wtf import FlaskForm
from wtforms import SubmitField, TextAreaField, StringField
from wtforms.validators import DataRequired, Length


class Feedback(FlaskForm):
    subject = StringField("Subject", validators=[DataRequired()])

    content = TextAreaField("Content", validators=[DataRequired(),Length(max=255)])

    submit = SubmitField("Submit")
