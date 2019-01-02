from flask import Blueprint, render_template

from Flask import db

main = Blueprint('main', __name__)


@main.route("/", methods=['GET', 'POST'])
def index():
    db.create_all()
    return render_template("home.html")