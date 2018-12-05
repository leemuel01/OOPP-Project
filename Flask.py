from flask import Flask, render_template, request, flash, url_for, redirect
from flask_mysqldb import MySQL

from Forms import Registration_Form, Login_Form   #Form classes
import yaml      #Database login and stuff

app = Flask(__name__)

#Security stuff so no cookie configuration
app.config["SECRET_KEY"] = '49dc263f9ebdbf0510c9273e5320e7df'

#Configure database
db = yaml.load(open("db.yaml"))
app.config['MYSQL_HOST'] = db['mysql_host']
app.config['MYSQL_USER'] = db['mysql_user']
app.config['MYSQL_PASSWORD'] = db['mysql_password']
app.config['MYSQL_DB'] = db['mysql_db']

mysql = MySQL(app)

#Flask pages
@app.route("/", methods=['GET', 'POST'])
def index():
    form = Registration_Form()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        # return redirect(url_for("index"))

    # if request.method == "POST":
    #     #Fetch the form data
    #     results = request.form
    #     username = results["name"]
    #     password = results["pw"]
    #     email = results["email"]
    #     fullname = results["fullname"]
    #     nric = results["nric"]
    #
    #     # return 'success'
    #
    #     cur = mysql.connection.cursor()
    #     cur.execute("INSERT INTO Users(Username, Password, Email, Full_Name, NRIC) VALUES(%s, %s, %s, %s, %s)", (username, password, email, fullname, nric))
    #     mysql.connection.commit()
    #     cur.close()



    return render_template("home.html", title="Home", form=form )

@app.route("/templates/register.html", methods = ['POST', 'GET'])

def register():

    form = Registration_Form()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for("home"))

    return render_template("register.html", title="Sign Up", form=form)

@app.route("/login", methods = ['POST', 'GET'])
def login():
    form = Login_Form()

    return render_template("login.html",  title="Login", form=form)




@app.route("/templates/Symptom Checker.html", methods = ['POST', 'GET'])
def check():
    title = "Symptom Checker"
    return render_template("Symptom Checker.html", title=title )

@app.route("/templates/trivia.html", methods = ['POST', 'GET'])
def trivia():
    title = "Medical Trivia"
    return render_template("trivia.html", title=title )

#====================================== Medical Teacher Page =========================================

@app.route("/templates/medical teacher.html", methods = ['POST', 'GET'])
def teacher():
    title = "Medical Tutor  "
    return render_template("medical teacher.html", title=title )

#====================================== Feedback Page =========================================

from Feedback import Feedback
@app.route("/templates/feedback.html", methods = ['POST', 'GET'])
def feedback():
    title = "Feedback"
    return render_template("feedback.html", title=title )



@app.route("/templates/Appointment.html", methods = ['POST', 'GET'])
def appointment():
    title = "Appointment"

    return render_template("appointment.html", title=title)

form= Feedback("joe","the lazy fox jumped into a ditch")
print(form.get_date())
print(form.get_wordcount())

if __name__ == "__main__":
    app.run(debug=True)
