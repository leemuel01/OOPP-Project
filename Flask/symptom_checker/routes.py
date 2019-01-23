from flask import flash, redirect, url_for, render_template, Blueprint, request
from Flask.symptom_checker.forms import Symptom_Checker_Form
import sqlite3

symptom_checker = Blueprint('symptom_checker', __name__)


@symptom_checker.route("/Symptom_Checker", methods=['POST', 'GET'])
def symptom_check():
    form = Symptom_Checker_Form()
    if form.validate_on_submit():

        symptom_checked_box = request.form.get("answers")
        print(symptom_checked_box)
        # return redirect(url_for('main.index'))
    return render_template("Symptom Checker/Symptom Checker.html", title="Symptom Checker", form=form)


@symptom_checker.route("/symptom", methods=['POST', 'GET'])
def symptom():
    symptom_database = sqlite3.connect("flask/site.db")
    symptom_checked_box = request.form.get("answer")
    data_symptom_answer = symptom_database.execute('SELECT symptom_answer FROM symptom WHERE id=?',(symptom_checked_box))
    for i in data_symptom_answer:
        data_symptom_answer = i[0]
    data_symptom_treatment = symptom_database.execute('SELECT symptom_treatment FROM symptom WHERE id=?',(symptom_checked_box))
    for r in data_symptom_treatment:
        data_symptom_treatment = r[0]
    return render_template("Symptom Checker/Symptom.html", title="Symptom Checker", test3=data_symptom_answer,
                           test4=data_symptom_treatment)

# <--- To take the data and put it at the symptom part at Symptom.html --->
# def select_answer:
#     symptom_database.execute('SELECT symptom_answer FROM symptom WHERE id=1')
#     data_symptom_answer = symptom_database.fetchone()
#     symptom_database.execute('SELECT symptom_treatment FROM symptom WHERE id=1')
#     data_symptom_treatment = symptom_database.fetchone()

# <--- To take the data and put it at the how to treat your symptom part at Symptom.html --->

