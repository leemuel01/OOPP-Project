from flask import Blueprint, render_template

trivia = Blueprint('trivia', __name__)

@trivia.route("/templates/trivia.html", methods = ['POST', 'GET'])
def main_page():
    title = "Medical Trivia"
    return render_template("Trivia/trivia.html", title=title )