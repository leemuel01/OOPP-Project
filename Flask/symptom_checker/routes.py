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


def symptom_onload():
    for_id = 1
    symptom_qa_database_onload = sqlite3.connect("flask/site.db")
    symptom_set_question_onload = symptom_qa_database_onload.execute('SELECT question FROM symptom_qa WHERE id=?', (for_id,))
    symptom_set_answer_one_onload = symptom_qa_database_onload.execute('SELECT answer_1 FROM symptom_qa WHERE id=?', (for_id,))
    symptom_set_answer_two_onload = symptom_qa_database_onload.execute('SELECT answer_2 FROM symptom_qa WHERE id=?', (for_id,))
    symptom_set_answer_three_onload = symptom_qa_database_onload.execute('SELECT answer_3 FROM symptom_qa WHERE id=?', (for_id,))
    symptom_set_answer_four_onload = symptom_qa_database_onload.execute('SELECT answer_4 FROM symptom_qa WHERE id=?', (for_id,))
    symptom_set_answer_five_onload = symptom_qa_database_onload.execute('SELECT answer_5 FROM symptom_qa WHERE id=?', (for_id,))
    for g in symptom_set_question_onload:
        symptom_set_question_onload = g[0]
    for h in symptom_set_answer_one_onload:
        symptom_set_answer_one_onload = h[0]
    for i in symptom_set_answer_two_onload:
        symptom_set_answer_two_onload = i[0]
    for j in symptom_set_answer_three_onload:
        symptom_set_answer_three_onload = j[0]
    for k in symptom_set_answer_four_onload:
        symptom_set_answer_four_onload = k[0]
    for l in symptom_set_answer_five_onload:
        symptom_set_answer_five_onload = l[0]
    return render_template("Symptom Checker/Symptom Checker.html", title="Symptom Checker", symptom_question_html=symptom_set_question_onload,
                           symptom_answer_one_html=symptom_set_answer_one_onload, symptom_answer_two_html=symptom_set_answer_two_onload,
                           symptom_answer_three_html=symptom_set_answer_three_onload, symptom_answer_four_html=symptom_set_answer_four_onload,
                           symptom_answer_five_html=symptom_set_answer_five_onload)


symptom_change_question_list = ['a']
symptom_answer_password = []


@symptom_checker.route("/symptom_change_question", methods=['POST', 'GET'])
def symptom_change_question():
    symptom_change_question_list_length = (len(symptom_change_question_list))
    symptom_qa_database = sqlite3.connect("flask/site.db")
    symptom_checked_box = request.form.get("answer")
    symptom_set_question = symptom_qa_database.execute('SELECT question FROM symptom_qa WHERE id=?', (symptom_change_question_list_length,))
    symptom_set_answer_one = symptom_qa_database.execute('SELECT answer_1 FROM symptom_qa WHERE id=?', (symptom_change_question_list_length,))
    symptom_set_answer_two = symptom_qa_database.execute('SELECT answer_2 FROM symptom_qa WHERE id=?', (symptom_change_question_list_length,))
    symptom_set_answer_three = symptom_qa_database.execute('SELECT answer_3 FROM symptom_qa WHERE id=?', (symptom_change_question_list_length,))
    symptom_set_answer_four = symptom_qa_database.execute('SELECT answer_4 FROM symptom_qa WHERE id=?', (symptom_change_question_list_length,))
    symptom_set_answer_five = symptom_qa_database.execute('SELECT answer_5 FROM symptom_qa WHERE id=?', (symptom_change_question_list_length,))
    for a in symptom_set_question:
        symptom_set_question = a[0]
    for b in symptom_set_answer_one:
        symptom_set_answer_one = b[0]
    for c in symptom_set_answer_two:
        symptom_set_answer_two = c[0]
    for d in symptom_set_answer_three:
        symptom_set_answer_three = d[0]
    for e in symptom_set_answer_four:
        symptom_set_answer_four = e[0]
    for f in symptom_set_answer_five:
        symptom_set_answer_five = f[0]
    if symptom_change_question_list_length <= 5:
        symptom_answer_password.append(symptom_checked_box)
        symptom_change_question_list.append(symptom_checked_box)
        return render_template("Symptom Checker/Symptom Checker.html", title="Symptom Checker", symptom_question_html=symptom_set_question,
                               symptom_answer_one_html=symptom_set_answer_one, symptom_answer_two_html=symptom_set_answer_two,
                               symptom_answer_three_html=symptom_set_answer_three, symptom_answer_four_html=symptom_set_answer_four,
                               symptom_answer_five_html=symptom_set_answer_five)
    symptom_get_answer_password = symptom_qa_database.execute('SELECT symptom_password FROM symptom')
    if len(symptom_answer_password) == 5:
        for m in symptom_get_answer_password:
            if m[0] == symptom_answer_password:
                symptom_for_if_loop = symptom_answer_password[m]
                data_symptom_answer = symptom_qa_database.execute('SELECT symptom_answer FROM symptom WHERE id=?', (symptom_for_if_loop,))
                for n in data_symptom_answer:
                    data_symptom_answer = n[0]
                data_symptom_treatment = symptom_qa_database.execute('SELECT symptom_treatment FROM symptom WHERE id=?', (symptom_for_if_loop,))
                for o in data_symptom_treatment:
                    data_symptom_treatment = o[0]
            else:
                data_symptom_unknown = 5
                data_symptom_answer = symptom_qa_database.execute('SELECT symptom_answer FROM symptom WHERE id=?', (data_symptom_unknown,))
                data_symptom_treatment = symptom_qa_database.execute('SELECT symptom_treatment FROM symptom WHERE id=?', (data_symptom_unknown,))
    if symptom_change_question_list_length >= 6:
        return render_template("Symptom Checker/Symptom.html", title="Symptom", symptom_reply_answer=data_symptom_answer,
                               symptom_reply_answer_treatment=data_symptom_treatment)


# def symptom_change_question():
#     symptom_question_password = []
#     symptom_qa_loop_set = 0
#     symptom_qa_database = sqlite3.connect("flask/site.db")
#     symptom_checked_box = request.form.get("answer")
#     symptom_question_password.append(symptom_checked_box)
#     data_symptom_qa_loop_password = symptom_qa_database.execute('SELECT symptom_qa_password FROM symptom_qa WHERE id=?', (symptom_checked_box))
#     for i in data_symptom_qa_loop_password:
#         data_symptom_qa_loop_password = i[symptom_qa_loop_set]
#         if data_symptom_qa_loop_password == symptom_question_password:
#             return render_template("Symptom Checker/Symptom Checker.html", title="Symptom Checker")
#         else:
#             symptom_qa_loop_set += 1

# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# @symptom_checker.route("/symptom", methods=['POST', 'GET'])
# def symptom():
#     symptom_database = sqlite3.connect("flask/site.db")
#     symptom_checked_box = request.form.get("answer")
#     data_symptom_answer = symptom_database.execute('SELECT symptom_answer FROM symptom WHERE id=?',(symptom_checked_box))
#     for i in data_symptom_answer:
#         data_symptom_answer = i[0]
#     data_symptom_treatment = symptom_database.execute('SELECT symptom_treatment FROM symptom WHERE id=?',(symptom_checked_box))
#     for r in data_symptom_treatment:
#         data_symptom_treatment = r[0]
#     return render_template("Symptom Checker/Symptom.html", title="Symptom Checker", test3=data_symptom_answer,
#                            test4=data_symptom_treatment)
# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# <--- To take the data and put it at the symptom part at Symptom.html --->
# def select_answer:
#     symptom_database.execute('SELECT symptom_answer FROM symptom WHERE id=1')
#     data_symptom_answer = symptom_database.fetchone()
#     symptom_database.execute('SELECT symptom_treatment FROM symptom WHERE id=1')
#     data_symptom_treatment = symptom_database.fetchone()

# <--- To take the data and put it at the how to treat your symptom part at Symptom.html --->

