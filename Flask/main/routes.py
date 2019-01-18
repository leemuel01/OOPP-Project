from datetime import datetime

from flask import Blueprint, render_template, flash
from Flask import db
from Flask.Models import User

main = Blueprint('main', __name__)


@main.route("/", methods=['GET', 'POST'])
def index():
    db.create_all()
    expired_users = User.query.filter(User.delete_time<=datetime.utcnow())
    for i in expired_users:
        if i.authenticated == False:
            db.session.delete(i)
            db.session.commit()
    return render_template("home.html")