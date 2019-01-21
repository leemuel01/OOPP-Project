from flask import flash, redirect, url_for, render_template, Blueprint
from Flask.symptom_checker.forms import Symptom_Checker_Form

symptom_checker = Blueprint('symptom_checker', __name__)

@symptom_checker.route("/Symptom Checker", methods = ['POST', 'GET'])
def symptom_check():
    form = Symptom_Checker_Form()
    if form.validate_on_submit():
        flash("banana", 'success')
        return redirect(url_for('main.index'))
    return render_template("SySymptom Checker/mptom Checker.html", title="Symptom Checker", form=form)