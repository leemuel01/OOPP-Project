from flask import Flask, render_template, request, flash, url_for, redirect
from feedback import Content
from feedback import Feedback
app = Flask(__name__)
app.config['SECRET_KEY']="12345"
@app.route("/", methods=['GET', 'POST'])
def index():
    title = "Home"


    return render_template("home.html", title=title )

@app.route("/results", methods = ['POST', 'GET'])

def profile():
    # student1 = Student("Test", "Male", "12345X")
    # student1.set_mark("70")

    if request.method == "POST":
        results = request.form

    return render_template("info.html",  result=results, student = student1)

@app.route("/templates/Symptom Checker.html", methods = ['POST', 'GET'])
def check():
    title = "Symptom Checker"
    return render_template("Symptom Checker.html", title=title )

@app.route("/templates/trivia.html", methods = ['POST', 'GET'])
def trivia():
    title = "Medical Trivia"
    return render_template("trivia.html", title=title )

@app.route("/templates/medical teacher.html", methods = ['POST', 'GET'])
def teacher():
    title = "Medical Tutor  "
    return render_template("medical teacher.html", title=title )

@app.route("/templates/feedback.html", methods = ['POST', 'GET'])
def feedback():
    title = "Feedback"
    form = Feedback()
    if form.validate_on_submit():



        flash(f'feedback submitted.', "success")
    return render_template("feedback.html", title=title, form = form)


# form = Feedback("joe","the lazy fox jumped into a ditch")
# print(form.get_date())
# print(form.get_wordcount())

if __name__ == "__main__":
    app.run(debug=True)



