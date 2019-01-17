from flask import Blueprint, render_template

medical_teacher = Blueprint('medical_teacher', __name__)

@medical_teacher.route("/Medical Teacher", methods = ['POST', 'GET'])
def teacher():
    title = "Medical Tutor  "
    return render_template("Medical Teacher/medical teacher.html", title=title )