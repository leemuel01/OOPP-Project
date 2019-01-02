from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField, TextAreaField, DateField, SelectField
from wtforms.validators import DataRequired, ValidationError, Optional


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

class Vaccine_History_Form(FlaskForm):
    vaccine_type = StringField('Allergy', validators=[])
    date = DateField('Admission Date', format='%d/%m/%Y')
    submit = SubmitField("Update")