import secrets
import os
from PIL import Image
from flask import render_template, flash, url_for, redirect, request
from Flask import app, db, bcrypt



from Flask.Forms import Registration_Form, Login_Form, Update_Account_Form, Personal_Profile_Form, Feedback   #Form classes
from Flask.Models import User, Personal_Profile, Content
from flask_login import login_user, current_user, logout_user, login_required

#Flask pages
@app.route("/", methods=['GET', 'POST'])
def index():

    return render_template("home.html")

@app.route("/templates/register.html", methods = ['POST', 'GET'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = Registration_Form()

    if form.validate_on_submit():

        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8') #encryption password

        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        #full_name=form.full_name.data, nric=form.nric.data

        #adding the user to database
        db.session.add(user)
        db.session.commit()

        flash(f'Your account has been created! You are now able to log in.', 'success')

        #get form data
        # username = form.username.data
        # password = form.password.data
        # email = form.email.data

        # fullname = form.full_name.data
        # nric = form.nric.data


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
    if current_user.is_authenticated:
        return redirect(url_for('index'))

    form = Login_Form()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()

        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for("index"))
        else:
            flash('Login unsuccessful. Please check username and password', 'danger')

    return render_template("login.html",  title="Login", form=form)

@app.route("/logout", methods = ['POST', 'GET'])
def logout():
    logout_user()
    return redirect(url_for("index"))



def save_picture(form_picture):
    #saving image and making the image name random
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_picture.filename)
    picture_fn = random_hex + f_ext
    picture_path = os.path.join(app.root_path, 'static/images/Profile_Picture', picture_fn)

    #resizes image to 200x200 px so it gets smaller. Saves memory too.
    output_size = (200,200)
    i = Image.open(form_picture)
    i.thumbnail(output_size)

    i.save(picture_path)

    return picture_fn


@app.route("/Profile", methods = ['POST', 'GET'])
@login_required
def account():

    image_files = url_for('static', filename=f"images/Profile_Picture/{current_user.image_file}")

    return render_template("profile.html", title="Profile",
                           image_file=image_files)


@app.route("/Profile/Reminder", methods = ['POST', 'GET'])
@login_required
def profile_reminder():
    image_files = url_for('static', filename=f"images/Profile_Picture/{current_user.image_file}")
    return render_template("profile.html", title="Reminder", image_file=image_files)


@app.route("/Profile/History", methods = ['POST', 'GET'])
@login_required
def profile_history():
    image_files = url_for('static', filename=f"images/Profile_Picture/{current_user.image_file}")
    return render_template("profile.html", title="History", image_file=image_files)


@app.route("/Profile/Edit", methods = ['POST', 'GET'])
@login_required
def profile_edit():

    form = Update_Account_Form()

    if form.validate_on_submit():
        if form.picture.data:
            picture_file = save_picture(form.picture.data)
            current_user.image_file = picture_file

        current_user.username = form.username.data
        current_user.email = form.email.data

        db.session.commit()
        flash('Your account has been updated!', 'success')
        return redirect(url_for('account'))

    elif request.method == 'GET':
        form.username.data = current_user.username
        form.email.data = current_user.email


    image_files = url_for('static', filename=f"images/Profile_Picture/{current_user.image_file}")

    return render_template("profile.html", title="Edit", image_file=image_files, form=form)



@app.route("/History", methods = ['POST', 'GET'])
@login_required

def Medical_History():
    user = User.query.filter_by(username=current_user.username).first()
    form = Personal_Profile_Form()

    if form.validate_on_submit():
        if user.personal_profile == None:
            history = Personal_Profile(full_name=form.full_name.data,
                                       nric=form.nric.data,
                                       age=form.birthday.data,
                                       sex=form.sex.data,
                                       address=form.address.data,
                                       user_id=current_user.id)
            db.session.add(history)

        else:
            current_user.personal_profile.nric = form.nric.data
            current_user.personal_profile.full_name = form.full_name.data
            current_user.personal_profile.age = form.birthday.data
            current_user.personal_profile.sex = form.sex.data
            current_user.personal_profile.address = form.address.data

        db.session.commit()
        flash(f'Your personal details have been updated', 'success')
        return redirect(url_for('account'))

    # elif user.personal_profile != None and request.method == 'GET':
    #     form.full_name.data = user.personal_profile.full_name
    #     form.nric.data = user.personal_profile.nric

    return render_template('edit medical history.html', title="Edit Medical History", form=form)





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
    form = Feedback()
    if form.validate_on_submit():
        content = Content(subject=form.subject.data, content=form.content.data)
        db.session.add(content)
        db.session.commit()


        flash(f'feedback submitted.', "success")
    return render_template("feedback.html", title=title, form = form)



#====================================== Appointment Page =========================================

@app.route("/Appointment", methods = ['POST', 'GET'])
def appointment():
    title = "Appointment"

    return render_template("appointment.html", title=title)
