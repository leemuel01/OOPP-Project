from flask import flash, redirect, url_for, render_template, Blueprint, request
import sqlite3

symptom_checker = Blueprint('symptom_checker', __name__)


@symptom_checker.route("/Symptom_Checker", methods=['POST', 'GET'])
def symptom_check():
    database = sqlite3.connect("flask/site.db")
    question_list = []
    get_answer = request.form.get("answer")
    if get_answer is None:
        answers_list = []
        answer_len = 0
    else:
        get_answer_list = request.form.get("answer_list")
        answers_list = eval(get_answer_list)
        answer_len = len(answers_list)+1

    question_obj = database.execute("SELECT * FROM symptom_qa WHERE id = ?", (answer_len+1,))

    for i in question_obj:
        question_list.append(i)

    if answer_len >=5:
        answers_list.append(get_answer)
        #sql wont take list need to convert to str
        symptom_string= str(answers_list)
        symptom_obj = database.execute("SELECT * FROM symptom where symptom_password = ?",(symptom_string,))
        check_symptom_empty=symptom_obj.fetchone()
        if check_symptom_empty is None:
            error_message = "Please see a doctor for your symptoms"
            return render_template("Symptom Checker/Symptom.html", title="Symptom Checker", error_msg=error_message)
        else:
            # run once more or else fetchone will make object empty for some reason
            symptom_obj = database.execute("SELECT * FROM symptom where symptom_password = ?", (symptom_string,))
            return render_template("Symptom Checker/Symptom.html", title="Symptom Checker", likely_ans=symptom_obj)

    elif get_answer is None:

        return render_template("Symptom Checker/Symptom Checker.html", title="Symptom Checker",
                               q_list=question_list, a_list=answers_list)
    elif get_answer is not None:
        answers_list.append(get_answer)
        return render_template("Symptom Checker/Symptom Checker.html", title="Symptom Checker",
                               q_list=question_list, a_list=answers_list)