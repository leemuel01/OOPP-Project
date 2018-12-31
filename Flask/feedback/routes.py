from flask import Blueprint, render_template, flash

from Flask import db
from Flask.Models import Content
from Flask.feedback.forms import Feedback

feedback = Blueprint('feedback', __name__)

@feedback.route("/Feedback", methods = ['POST', 'GET'])
def form_page():
    title = "Feedback"
    form = Feedback()
    if form.validate_on_submit():
        content = Content(subject=form.subject.data, content=form.content.data)
        db.session.add(content)
        db.session.commit()


        flash(f'feedback submitted.', "success")

    return render_template("Feedback/feedback.html", title=title, form = form)