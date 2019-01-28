from flask_login import current_user
from flask_wtf import FlaskForm
from flask_wtf.file import FileAllowed
from wtforms import StringField, PasswordField, BooleanField, SubmitField, FileField, DateField, DateTimeField
from wtforms.validators import DataRequired, Length, EqualTo, Email, ValidationError, Optional

from Flask.Models import User


class Registration_Form(FlaskForm):

    username = StringField("Username",
                           validators=[DataRequired(), Length(min=2, max=20)])

    password = PasswordField("Password",
                             validators=[DataRequired(), Length(min=6)])

    confirm_password = PasswordField("Confirm Password",
                                     validators=[DataRequired(), EqualTo("password")])

    email = StringField('Email',
                        validators=[DataRequired(), Email()])



    submit = SubmitField('Sign Up')

    #=============================== Validators to check whether stuff exist in database already ==========================

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError("Username is already taken.")

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError("Email is already taken.")

class Login_Form(FlaskForm):

    username = StringField("Username",
                           validators=[DataRequired()])

    password = PasswordField("Password",
                             validators=[DataRequired()])

    remember = BooleanField("Remember Me")
    submit = SubmitField('Login')

class Update_Account_Form(FlaskForm):

    username = StringField("Username",
                           validators=[DataRequired(), Length(min=2, max=20)])

    email = StringField('Email',
                        validators=[DataRequired(), Email()])

    picture = FileField('Update Profile Picture', validators=[FileAllowed(['jpg', 'png', 'gif'])])

    submit = SubmitField('Update')

    #=============================== Validators to check whether stuff exist in database already ==========================

    def validate_username(self, username):
        if username.data != current_user.username:
            user = User.query.filter_by(username=username.data).first()
            if user:
                raise ValidationError("Username is already taken.")

    def validate_email(self, email):
        if email.data != current_user.email:
            user = User.query.filter_by(email=email.data).first()
            if user:
                raise ValidationError("Email is already taken.")


class Request_Reset_Form(FlaskForm):
    email = StringField('Email',
                        validators=[DataRequired(), Email()])

    submit = SubmitField('Request Password Reset')


    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is None:
            raise ValidationError("There is no account with that email. You must register first.")


class Reset_Password_Form(FlaskForm):
    password = PasswordField("Password",
                             validators=[DataRequired(), Length(min=6)])

    confirm_password = PasswordField("Confirm Password",
                                     validators=[DataRequired(), EqualTo("password")])

    submit = SubmitField('Reset Password')

class Reminder_Form(FlaskForm):
    reminder = StringField('Reminder', validators=[])
    reminder_date = DateTimeField('Date', format='%d/%m/%Y %H:%M', validators=[Optional()])
    submit = SubmitField("Add")



