from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from flask_login import current_user
from wtforms import StringField, PasswordField, SubmitField, BooleanField, DateTimeField, SelectField, TextAreaField, DateField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError

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

    # def validate_nric(self, nric):
    #     user = User.query.filter_by(nric=nric.data).first()
    #     if user:
    #         raise ValidationError("NRIC is already taken.")



class Login_Form(FlaskForm):

    username = StringField("Username",
                           validators=[DataRequired(), Length(min=2, max=20)])
    # email = StringField('Email',
    #                     validators=[DataRequired(), Email()])
    password = PasswordField("Password",
                             validators=[DataRequired(), Length(min=6)])
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

    def validate_nric(self, nric):
        if nric.data != current_user.nric:
            user = User.query.filter_by(nric=nric.data).first()
            if user:
                raise ValidationError("NRIC is already taken.")


#====================================================================================================================================
#====================================================================================================================================
#====================================================================================================================================

class Personal_Profile_Form(FlaskForm):
    full_name = StringField("Full Name",
                            validators=[])

    nric = StringField("NRIC",
                       validators=[
                           # Length(min=9, max=9, message="Please enter a valid NRIC")
                       ])

    birthday = DateField('Date of Birth', format='%d/%m/%Y')

    sex = SelectField("Sex", choices=[('Male', 'Male'), ('Female', 'Female'), ('Others', 'Others')])

    address = TextAreaField("Address", validators=[])

    submit = SubmitField('Update')
#feedback
class Feedback(FlaskForm):
    subject = StringField("Subject", validators=[DataRequired()])

    content = TextAreaField("Content", validators=[DataRequired(),Length(max=255)])

    submit = SubmitField("Submit")