from flask_wtf import FlaskForm
from wtforms import StringField , SubmitField,TextAreaField
from wtforms.validators import DataRequired, Length

class Feedback(FlaskForm):
    subject = StringField("Subject", validators=[DataRequired()])

    content = TextAreaField("Content", validators=[DataRequired(),Length(max=255)])

    submit = SubmitField("Submit")





