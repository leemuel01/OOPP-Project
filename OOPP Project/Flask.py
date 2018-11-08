from flask import Flask, render_template, request, flash, url_for, redirect
from Student import Student
app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def index():
    title = "Home"


    return render_template("home.html", title=title )

@app.route("/results", methods = ['POST', 'GET'])

def profile():
    student1 = Student("Test", "Male", "12345X")
    # student1.set_mark("70")


    if request.method == "POST":
        results = request.form

    return render_template("info.html",  result=results, student = student1)

if __name__ == "__main__":
    app.run(debug=True)
