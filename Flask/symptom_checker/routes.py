from flask import flash, redirect, url_for, render_template, Blueprint
from Flask.symptom_checker.forms import Symptom_Checker_Form

symptom_checker = Blueprint('symptom_checker', __name__)


@symptom_checker.route("/Symptom Checker", methods = ['POST', 'GET'])
def symptom_check():
    form = Symptom_Checker_Form()
    if form.validate_on_submit():
        flash("banana", 'success')
        return redirect(url_for('main.index'))
    return render_template("Symptom Checker/Symptom Checker.html", title="Symptom Checker", form=form)


# <--- To take the data and put it at the symptom part at Symptom.html --->
# def select_answer:
#     <variable>.execute('SELECT symptom_answer FROM symptom')
#     data_symptom_answer = <variable>.fetchall()
#     print(data_symptom_answer)

# <--- To take the data and put it at the how to treat your symptom part at Symptom.html --->
#     <variable>.execute('SELECT symptom_treatment FROM symptom')
#     data_symptom_treatment = <variable>.fetchall()
#     print(data_symptom_treatment)
