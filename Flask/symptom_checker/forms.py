from flask_wtf import FlaskForm
from wtforms import RadioField, SubmitField


class Symptom_Checker_Form(FlaskForm):
    answers = RadioField('Label', choices=[('value', 'one'), ('value_two', 'two'),
                                           ('value_three', 'three'), ('value_four', 'four')])
    submit = SubmitField("Submit")
