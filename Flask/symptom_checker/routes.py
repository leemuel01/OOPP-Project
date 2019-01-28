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


@symptom_checker.route("/symptom_change_question", methods=['POST', 'GET'])
def symptom_change_question():

    symptom_change_question_list = [1]
    symptom_change_question_list_length = (len(symptom_change_question_list))
    symptom_qa_database = sqlite3.connect("flask/site.db")
    symptom_checked_box = request.form.get("answer")
    symptom_set_question = symptom_qa_database.execute('SELECT question FROM symptom_qa WHERE id=?',
                                                       (symptom_change_question_list_length,))

    symptom_set_answer_one = symptom_qa_database.execute('SELECT answer_1 FROM symptom_qa WHERE id=?',
                                                         (symptom_change_question_list_length,))

    symptom_set_answer_two = symptom_qa_database.execute('SELECT answer_2 FROM symptom_qa WHERE id=?',
                                                         (symptom_change_question_list_length,))

    symptom_set_answer_three = symptom_qa_database.execute('SELECT answer_3 FROM symptom_qa WHERE id=?',
                                                           (symptom_change_question_list_length,))

    symptom_set_answer_four = symptom_qa_database.execute('SELECT answer_4 FROM symptom_qa WHERE id=?',
                                                          (symptom_change_question_list_length,))

    symptom_set_answer_five = symptom_qa_database.execute('SELECT answer_5 FROM symptom_qa WHERE id=?',
                                                          (symptom_change_question_list_length,))

    if int(symptom_checked_box) > 0:
        symptom_change_question_list.append(symptom_checked_box)

    if symptom_change_question_list_length < 6:
        return render_template("Symptom Checker/Symptom Checker.html", title="Symptom Checker", symptom_question_html=symptom_set_question,
                               symptom_answer_one_html=symptom_set_answer_one, symptom_answer_two_html=symptom_set_answer_two,
                               symptom_answer_three_html=symptom_set_answer_three, symptom_answer_four_html=symptom_set_answer_four,
                               symptom_answer_five_html=symptom_set_answer_five)
    # else:
    #     return render_template("Symptom Checker/Symptom.html", title="Symptom", symptom_reply_answer=data_symptom_answer,
    #                            symptom_reply_answer_treatment=data_symptom_treatment)





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

