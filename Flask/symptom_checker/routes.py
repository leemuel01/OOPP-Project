from flask import flash, redirect, url_for, render_template, Blueprint, request
from Flask.symptom_checker.forms import Symptom_Checker_Form
import sqlite3

symptom_checker = Blueprint('symptom_checker', __name__)
symptom_database = sqlite3.connect("../site.db")


@symptom_checker.route("/Symptom Checker", methods = ['POST', 'GET'])
def symptom_check():
    form = Symptom_Checker_Form()
    if form.validate_on_submit():
        symptom_checked_box = request.form.get("answers")
        print(symptom_checked_box)
        # return redirect(url_for('main.index'))
    return render_template("Symptom Checker/Symptom Checker.html", title="Symptom Checker", form=form)


# <--- To take the data and put it at the symptom part at Symptom.html --->
# def select_answer:
#     symptom_database.execute('SELECT symptom_answer FROM symptom')
#     data_symptom_answer = symptom_database.fetchall()
#     print(data_symptom_answer)

# <--- To take the data and put it at the how to treat your symptom part at Symptom.html --->
#     symptom_database.execute('SELECT symptom_treatment FROM symptom')
#     data_symptom_treatment = symptom_database.fetchall()
#     print(data_symptom_treatment)
