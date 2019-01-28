from datetime import datetime

from flask import Blueprint, render_template, flash
from Flask import db
from Flask.Models import User



from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_wtf import Form
from wtforms.fields import DateField

main = Blueprint('main', __name__)


class MyForm(Form):
    date = DateField(id='datepick')

@main.route('/test')
def test():
    form = MyForm()

    return render_template('text.html', form=form)


@main.route("/", methods=['GET', 'POST'])
def index():
    expired_users = User.query.filter(User.delete_time<=datetime.now())
    for i in expired_users:
        if i.authenticated == False:
            db.session.delete(i)
            db.session.commit()

    return render_template("home.html")