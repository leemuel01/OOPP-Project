from flask import flash, redirect, url_for, render_template, Blueprint
from Flask.symptom_checker.forms import Symptom_Checker_Form
from flask_sqlalchemy import SQLAlchemy

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///symptom.db'
db = SQLAlchemy(app)


class SymptomAnswer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    symptom_answer = db.Column(nullable=False)

    def __repr__(self):
        return f"{self.symptom_answer}"


class SymptomTreatment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    symptom_treatment = db.Column(nullable=False)

    def __repr__(self):
        return f"{self.symptom_treatment}"


symptom_checker = Blueprint('symptom_checker', __name__)


@symptom_checker.route("/Symptom Checker", methods = ['POST', 'GET'])
def symptom_check():
    form = Symptom_Checker_Form()
    if form.validate_on_submit():
        flash("banana", 'success')
        return redirect(url_for('main.index'))
    return render_template("SySymptom Checker/mptom Checker.html", title="Symptom Checker", form=form)
