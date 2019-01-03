from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class ReviewForm(FlaskForm):
    comment = StringField('Leave a review',
                          validators=[DataRequired()])
submit = SubmitField('Submit')
