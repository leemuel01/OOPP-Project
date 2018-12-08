from flask import render_template, flash, url_for, redirect
from Flask import app, db, bcrypt

from Flask.Forms import Registration_Form, Login_Form   #Form classes
from Flask.Feedback import Feedback
from Flask.Models import User, History

#Flask pages
@app.route("/", methods=['GET', 'POST'])
def index():

    return render_template("home.html")

@app.route("/templates/register.html", methods = ['POST', 'GET'])
def register():

    form = Registration_Form()
    if form.validate_on_submit():

        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8') #encryption password

        user = User(username=form.username.data, email=form.email.data, password=hashed_password, full_name=form.full_name.data, nric=form.nric.data)

        #adding the user to database
        db.session.add(user)
        db.session.commit()

        flash(f'Your account has been created! You are not able to log in.', 'success')

        #get form data
        username = form.username.data
        password = form.password.data
        email = form.email.data
        fullname = form.full_name.data
        nric = form.nric.data


        # #flask-mysqldb stuff
        # cur = mysql.connection.cursor()
        # cur.execute("INSERT INTO Users(Username, Password, Email, Full_Name, NRIC) VALUES(%s, %s, %s, %s, %s)",
        #             (username, password, email, fullname, nric))
        # mysql.connection.commit()
        # cur.close()
        return redirect(url_for("login"))



    return render_template("register.html", title="Sign Up", form=form)

@app.route("/Login", methods = ['POST', 'GET'])
def login():

    form = Login_Form()
    if form.validate_on_submit():
        if form.username.data == 'test' and form.password.data == '12345678':
            flash('You have been logged in!', 'success')
            return redirect(url_for("index"))

        else:
            flash('Login unsuccessful.', 'danger')

    return render_template("login.html",  title="Login", form=form)


@app.route("/Symptom Checker", methods = ['POST', 'GET'])
def symptom_checker():
    title = "Symptom Checker"
    return render_template("Symptom Checker.html", title=title )

@app.route("/templates/trivia.html", methods = ['POST', 'GET'])
def trivia():
    title = "Medical Trivia"
    return render_template("trivia.html", title=title )


#====================================== Medical Teacher Page =========================================

@app.route("/Medical Teacher", methods = ['POST', 'GET'])
def teacher():
    title = "Medical Tutor  "
    return render_template("medical teacher.html", title=title )


#====================================== Feedback Page =========================================

@app.route("/Feedback", methods = ['POST', 'GET'])
def feedback():
    title = "Feedback"
    return render_template("feedback.html", title=title )



#====================================== Appointment Page =========================================

@app.route("/Appointment", methods = ['POST', 'GET'])
def appointment():
    title = "Appointment"

    return render_template("appointment.html", title=title)
