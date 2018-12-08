from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo

class Registration_Form(FlaskForm):

    username = StringField("Username",
                           validators=[DataRequired(), Length(min=2, max=20)])

    password = PasswordField("Password",
                             validators=[DataRequired(), Length(min=6)])

    confirm_password = PasswordField("Confirm Password",
                                     validators=[DataRequired(), EqualTo("password")])

    email = StringField('Email',
                        validators=[DataRequired(), Email()])

    full_name = StringField("Full Name",
                            validators=[DataRequired()])

    nric = StringField("NRIC",
                       validators=[DataRequired(), Length(min=9, max=9, message="Please enter a valid NRIC")])

    submit = SubmitField('Sign Up')


class Login_Form(FlaskForm):
    username = StringField("Username",
                           validators=[DataRequired(), Length(min=2, max=20)])
    # email = StringField('Email',
    #                     validators=[DataRequired(), Email()])
    password = PasswordField("Password",
                             validators=[DataRequired(), Length(min=6)])
    remember = BooleanField("Remember Me")
    submit = SubmitField('Login')

