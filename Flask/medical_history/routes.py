import datetime
import pdfkit

from flask import Blueprint, redirect, url_for, flash, render_template, request, make_response
from flask_login import login_required, current_user

from Flask import db
from Flask.Models import Blood_Transfusions, Allergies, Surgeries, Admissions, Personal_Profile, Vaccinations, Illnesses
from Flask.medical_history.forms import Blood_Transfusion_History_Form, Allergy_History_Form, Previous_Surgeries_Form, \
    Previous_Admissions_Form, Personal_Profile_Form, Vaccine_History_Form, Previous_Illnesses_Form
from Flask.medical_history.hospitals import choices

medical_history = Blueprint('medical_history', __name__)

@medical_history.route("/History", methods = ['POST', 'GET'])
@login_required
def Personal_Details():
    form = Personal_Profile_Form()

    if form.validate_on_submit():
        age = int(datetime.datetime.today().year) - \
              int(form.birthday.data.year - ((datetime.datetime.today().month, datetime.datetime.today().day) > (form.birthday.data.month, form.birthday.data.day))) - 1

        bmi = form.weight.data / (form.height.data ** 2)
        # flash(f"{.year()}")

        if current_user.personal_profile == []:

            history = Personal_Profile(full_name=form.full_name.data,
                                       nric=form.nric.data,
                                       birthday=form.birthday.data,
                                       sex=form.sex.data,
                                       address=form.address.data,
                                       age= age,
                                       height=form.height.data,
                                       weight=form.weight.data,
                                       heart_rate=form.heart_rate.data,
                                       bmi= (round(bmi,2)),
                                       user_id=current_user.id)

            db.session.add(history)

        else:
            current_user.personal_profile[0].nric = form.nric.data
            current_user.personal_profile[0].full_name = form.full_name.data
            current_user.personal_profile[0].birthday = form.birthday.data
            current_user.personal_profile[0].sex = form.sex.data
            current_user.personal_profile[0].address = form.address.data

            current_user.personal_profile[0].age = age
            current_user.personal_profile[0].height = form.height.data
            current_user.personal_profile[0].weight = form.weight.data
            current_user.personal_profile[0].heart_rate = form.heart_rate.data
            current_user.personal_profile[0].bmi = (round(bmi,2))

        db.session.commit()

        flash(f'Your personal details have been updated', 'success')
        return redirect(url_for('users.profile_history'))

    elif current_user.personal_profile != [] and request.method == 'GET':

        form.full_name.data = current_user.personal_profile[0].full_name
        form.nric.data = current_user.personal_profile[0].nric
        form.birthday.data = current_user.personal_profile[0].birthday
        form.sex.data = current_user.personal_profile[0].sex
        form.address.data = current_user.personal_profile[0].address
        form.height.data = current_user.personal_profile[0].height
        form.weight.data = current_user.personal_profile[0].weight
        form.heart_rate.data = current_user.personal_profile[0].heart_rate

    return render_template('Medical History/edit personal details.html', title="Update Personal Details", form=form)


@medical_history.route("/Update <string:record>", methods=['POST', 'GET'])
@login_required
def Update_Record(record):
    records = {"Admissions": [Admissions, Previous_Admissions_Form()],
               "Illnesses": [Illnesses, Previous_Illnesses_Form()],
               "Surgeries": [Surgeries, Previous_Surgeries_Form()],
               "Blood Transfusions": [Blood_Transfusions, Blood_Transfusion_History_Form()],
               "Allergies": [Allergies, Allergy_History_Form()],
               "Vaccinations": [Vaccinations, Vaccine_History_Form()]
               }

    form = records[record][1]
    if records[record][0] in [Admissions, Blood_Transfusions, Surgeries]:
        form.place.choices = [(i, i) for i in choices]
    model = records[record][0]
    if form.validate_on_submit():
        if record == "Admissions":
            data = model(reason=form.reason.data,
                         date=form.date.data,
                         place=form.place.data,
                         comments=form.comment.data,
                         user_id=current_user.id)

        elif record == "Surgeries":
            data = model(date=form.date.data,
                                surgery_type=form.surgery_type.data,
                                place=form.place.data,
                                comments=form.comment.data,
                                user_id=current_user.id)

        elif record == "Blood Transfusions":
            data = model(date=form.date.data,
                                             blood_type=form.blood_type.data,
                                             place=form.place.data,
                                             comments=form.comment.data,
                                             user_id=current_user.id)

        elif record == "Allergies":
            data = model(date=form.date.data,
                                  allergy=form.allergy_type.data,
                                  user_id=current_user.id)

        elif record == "Vaccinations":
            data = model(date=form.date.data,
                                        vaccine=form.vaccine_type.data,
                                        user_id=current_user.id)

        elif record == "Illnesses":
            data = model(illness=form.illness.data, date=form.date.data, user_id=current_user.id)

        db.session.add(data)
        db.session.commit()
        flash(f'Your personal details have been updated', 'success')
        return redirect(url_for('medical_history.Update_Record', record=record))

    else:
        form.date.data = datetime.datetime.now()

    return render_template('Medical History/update forms.html', title=f"Update {record}", form=form)


@medical_history.route("/Update_<string:record>/<int:item_id>", methods = ['POST', 'GET'])
@login_required
def delete_item(record, item_id):
    records = {"Admissions": [Admissions, Previous_Admissions_Form()],
               "Illnesses": [Illnesses, Previous_Illnesses_Form()],
               "Surgeries": [Surgeries, Previous_Surgeries_Form()],
               "Blood Transfusions": [Blood_Transfusions, Blood_Transfusion_History_Form()],
               "Allergies": [Allergies, Allergy_History_Form()],
               "Vaccinations": [Vaccinations, Vaccine_History_Form()]
               }

    item = records[record][0].query.get_or_404(item_id)
    db.session.delete(item)
    db.session.commit()
    flash(f'The record has been successfully deleted!', 'success')
    return redirect(url_for('medical_history.Update_Record', record=record))


#Printing HTML to PDF uses pdfkit and wkhtmltopdf

@medical_history.route("/Print")
@login_required
def print_pdf():
    rendered = render_template('Medical History/pdf.html')

    config = pdfkit.configuration(wkhtmltopdf='wkhtmltopdf/bin/wkhtmltopdf.exe') #path to wkhtmltopdf app
    pdf = pdfkit.from_string(rendered, False, configuration=config)

    response = make_response(pdf)
    response.headers['Content-Type'] = 'application/pdf'
    response.headers['Content-Disposition'] = 'inline; filename=history.pdf'
    return response