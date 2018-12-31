from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from flask_login import current_user
from wtforms import StringField, PasswordField, SubmitField, BooleanField, DateTimeField, SelectField, TextAreaField, DateField, RadioField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError, Optional

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



#====================================================================================================================================
#====================================================================================================================================
#====================================================================================================================================

class Personal_Profile_Form(FlaskForm):
    full_name = StringField("Full Name",
                            validators=[])

    nric = StringField("NRIC",
                       validators=[])

    birthday = DateField('Date of Birth', format='%d/%m/%Y', validators=[Optional()])

    sex = SelectField("Sex", choices=[('Not Set', "Not Set"), ('Male', 'Male'), ('Female', 'Female'), ('Others', 'Others')], validators=[])

    address = TextAreaField("Address", validators=[])

    submit = SubmitField('Update')

    # =============================== Custom Validator ==========================

    def validate_nric(self, nric):
        if nric.data and len(nric.data) != 9:
            raise ValidationError("Please input a valid NRIC")

    def validate_birthday(self, birthday):
        if birthday.data:
            pass

# region Medical History Forms
class Previous_Admissions_Form(FlaskForm):

    place = TextAreaField("Place", validators=[DataRequired()])
    date = DateField('Admission Date', format='%d/%m/%Y')
    comment = TextAreaField("Comment", validators=[])
    submit = SubmitField("Update")


class Previous_Surgeries_Form(FlaskForm):
    surgery_type = StringField('Surgery Type', validators=[])
    date = DateField('Date', format='%d/%m/%Y')
    place = TextAreaField("Place", validators=[])
    comment = TextAreaField("Comment", validators=[])
    submit = SubmitField("Update")

class Blood_Transfusion_History_Form(FlaskForm):
    blood_type = StringField('Blood Type', validators=[])
    date = DateField('Date', format='%d/%m/%Y')
    place = TextAreaField("Place", validators=[])
    comment = TextAreaField("Comment", validators=[])
    submit = SubmitField("Update")

class Allergy_History_Form(FlaskForm):
    allergy_type = StringField('Allergy', validators=[])
    date = DateField('Admission Date', format='%d/%m/%Y')
    submit = SubmitField("Update")
# endregion

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



# region Teammates' forms
class ReviewForm(FlaskForm):
    comment = StringField('Leave a review',
                          validators=[DataRequired()])
submit = SubmitField('Submit')



class Feedback(FlaskForm):
    subject = StringField("Subject", validators=[DataRequired()])

    content = TextAreaField("Content", validators=[DataRequired(),Length(max=255)])

    submit = SubmitField("Submit")


class Symptom_Checker_Form(FlaskForm):
    answers = RadioField('Label', choices=[('value', 'one'), ('value_two', 'two'),
                                           ('value_three', 'three'), ('value_four', 'four')])
    submit = SubmitField("Submit")
# endregion