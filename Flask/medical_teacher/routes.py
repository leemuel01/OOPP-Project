from flask import Blueprint, render_template
from Flask.medical_teacher.medical_teacher import display_review
import sqlite3, request, datetime

medical_teacher = Blueprint('medical_teacher', __name__)

@medical_teacher.route("/Medical Teacher", methods = ['POST', 'GET'])
def teacher():
    title = "Medical Tutor "
    return render_template("Medical Teacher/medical teacher.html", title=title, display_review=display_review())


@medical_teacher.route('/handle_data', methods=['POST'])
def handle_data():
    sqlite_connection = sqlite3.connect("Flask/site.db")
    review_display = sqlite_connection.execute("select * from post_review where id=2")
    variable1 = request.form.get("project")
    form_date_now = datetime.datetime.now()
    post_comment = sqlite_connection.execute("insert into review_table_name(content,date_posted) values (?,?)"
                                          , (variable1, form_date_now))
