import datetime

from flask import Blueprint, redirect, url_for, flash, render_template, request
from flask_login import login_required, current_user

from Flask import db
from Flask.Models import Blood_Transfusions, Allergies, Surgeries, Admissions, Personal_Profile
from Flask.medical_history.forms import Blood_Transfusion_History_Form, Allergy_History_Form, Previous_Surgeries_Form, \
    Previous_Admissions_Form, Personal_Profile_Form

medical_history = Blueprint('medical_history', __name__)

@medical_history.route("/History", methods = ['POST', 'GET'])
@login_required
def Personal_Details():
    form = Personal_Profile_Form()

    if form.validate_on_submit():
        if current_user.personal_profile == []:

            history = Personal_Profile(full_name=form.full_name.data,
                                       nric=form.nric.data,
                                       birthday=form.birthday.data,
                                       sex=form.sex.data,
                                       address=form.address.data,
                                       user_id=current_user.id)

            db.session.add(history)

        else:
            current_user.personal_profile[0].nric = form.nric.data
            current_user.personal_profile[0].full_name = form.full_name.data
            current_user.personal_profile[0].birthday = form.birthday.data
            current_user.personal_profile[0].sex = form.sex.data
            current_user.personal_profile[0].address = form.address.data

        db.session.commit()

        flash(f'Your personal details have been updated', 'success')
        return redirect(url_for('users.account'))

    elif current_user.personal_profile != [] and request.method == 'GET':
        form.full_name.data = current_user.personal_profile[0].full_name
        form.nric.data = current_user.personal_profile[0].nric
        form.birthday.data = current_user.personal_profile[0].birthday
        form.sex.data = current_user.personal_profile[0].sex
        form.address.data = current_user.personal_profile[0].address

    return render_template('Medical History/edit personal details.html', title="Update Personal Details", form=form)


@medical_history.route("/UpdateAdmissions", methods = ['POST', 'GET'])
@login_required
def Previous_Admissions():
    form = Previous_Admissions_Form()

    if form.validate_on_submit():

        admission = Admissions(date=form.date.data,
                               place=form.place.data,
                               comments=form.comment.data,
                               user_id=current_user.id)

        db.session.add(admission)
        db.session.commit()
        flash(f'Your personal details have been updated', 'success')
        return redirect(url_for('medical_history.Previous_Admissions'))
    else:
        form.date.data = datetime.datetime.utcnow()


    return render_template('Medical History/update forms.html', title="Update Admissions", form=form)

@medical_history.route("/UpdateAdmissions/<int:item_id>", methods = ['POST', 'GET'])
@login_required
def delete_item(item_id):

    # item = Admissions.query.filter_by(id=item_id).first()
    item = Admissions.query.get_or_404(item_id)
    db.session.delete(item)
    db.session.commit()
    flash(f'Admission has been successfully deleted!', 'success')
    return redirect(url_for('medical_history.Previous_Admissions'))



@medical_history.route("/UpdateSurgeries", methods = ['POST', 'GET'])
@login_required
def Previous_Surgeries():
    form = Previous_Surgeries_Form()
    if form.validate_on_submit():

        surgery = Surgeries(date=form.date.data,
                            surgery_type=form.surgery_type.data,
                            place=form.place.data,
                            comments=form.comment.data,
                            user_id=current_user.id)

        db.session.add(surgery)
        db.session.commit()
        flash(f'Your personal details have been updated', 'success')
        return redirect(url_for('medical_history.profile_history'))
    else:
        form.date.data = datetime.datetime.utcnow()

    return render_template('Medical History/update forms.html', title="Update Surgeries", form=form)

@medical_history.route("/UpdateBloodTransfusion", methods = ['POST', 'GET'])
@login_required
def Blood_Transfusion_History():
    form = Blood_Transfusion_History_Form()

    if form.validate_on_submit():

        transfusion = Blood_Transfusions(date=form.date.data,
                            blood_type=form.blood_type.data,
                            place=form.place.data,
                            comments=form.comment.data,
                            user_id=current_user.id)

        db.session.add(transfusion)
        db.session.commit()
        flash(f'Your personal details have been updated', 'success')
        return redirect(url_for('medical_history.profile_history'))
    else:
        form.date.data = datetime.datetime.utcnow()

    return render_template('Medical History/update forms.html', title="Update Blood Transfusion", form=form)


@medical_history.route("/UpdateAllergies", methods = ['POST', 'GET'])
@login_required
def Update_Allergies():
    form = Allergy_History_Form()

    if form.validate_on_submit():
        allergies = Allergies(date=form.date.data, allergy=form.allergy_type.data, user_id=current_user.id)
        db.session.add(allergies)
        db.session.commit()
        flash(f'Your personal details have been updated', 'success')
        return redirect(url_for('medical_history.profile_history'))
    else:
        form.date.data = datetime.datetime.utcnow()

        return render_template('Medical History/update forms.html', title="Update Allergies", form=form)