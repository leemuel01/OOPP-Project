from flask import Blueprint, render_template, request
from Flask.medical_teacher.medical_teacher import MedicalTeacher
import sqlite3, datetime
from flask_login import login_user, logout_user, login_required, current_user
medical_teacher = Blueprint('medical_teacher', __name__)



@medical_teacher.route("/Medical Teacher", methods = ['POST', 'GET'])
def teacher():
    title = "Medical Tutor "
    health = MedicalTeacher()
    return render_template("Medical Teacher/medical teacher.html", title=title, display_review=health.display_review())


@medical_teacher.route('/handle_data', methods=['POST'])
def handle_data():
    sqlite_connection = sqlite3.connect("Flask/site.db")
    health = MedicalTeacher()
    user_id = current_user.get_id()
    profile_picture = current_user.image_file
    username = current_user.username
    review_display = sqlite_connection.execute("select * from post_review where id=2")
    variable1 = request.form.get("project")
    form_date_now = datetime.datetime.now().date()
    post_comment = sqlite_connection.execute\
        ("insert into post_review(content,date_posted,user_id,profile_picture,username)"
                                             " values (?,?,?,?,?)", (variable1, form_date_now
                                                                              , user_id, profile_picture, username))
    sqlite_connection.commit()
    return render_template("Medical Teacher/handle_data.html",display_var=variable1
                           , display_review=health.display_review())
