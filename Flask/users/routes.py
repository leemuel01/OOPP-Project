import datetime

from flask import Blueprint, redirect, url_for, render_template, request, flash
from flask_login import login_user, logout_user, login_required, current_user
from flask_wtf import Form
from wtforms import DateField

from Flask import bcrypt, db
from Flask.Models import User, Reminders
from Flask.users.forms import Registration_Form, Login_Form, Request_Reset_Form, Reset_Password_Form, \
    Update_Account_Form, Reminder_Form
from Flask.users.functions import send_reset_email, save_picture, send_authenticate_email, del_unauthenticated

import time
import atexit
# from apscheduler.schedulers.background import BackgroundScheduler
from flask_apscheduler.scheduler import BackgroundScheduler
users = Blueprint('users', __name__)

@users.route("/templates/register.html", methods = ['POST', 'GET'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))
    form = Registration_Form()

    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8') #encryption password
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)

        db.session.add(user)
        db.session.commit()

        email = User.query.filter_by(email=form.email.data).first()
        send_authenticate_email(email)

        flash(f'Your account has been created! Please check your email to activate it to log in.', 'success')
        return redirect(url_for("users.login"))

    return render_template("Users/register.html", title="Sign Up", form=form)

@users.route("/Login", methods = ['POST', 'GET'])
def login():
    if current_user.is_authenticated:

        return redirect(url_for('main.index'))

    form = Login_Form()

    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            if user.authenticated == 1:
                login_user(user, remember=form.remember.data)
                next_page = request.args.get('next')
                return redirect(next_page) if next_page else redirect(url_for("main.index"))
            else:
                flash('Please check your email to activate your account', 'success')


        else:
            flash('Login unsuccessful. Please check username and password', 'danger')

    return render_template("Users/login.html",  title="Login", form=form)

@users.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("main.index"))



@users.route("/authenticate/<token>")
def authenticate(token):

    user = User.verify_reset_token(token)
    if user == None:
        flash('That is an invalid or expired token.', 'warning')
        return redirect(url_for('users.register'))

    user.authenticated = True
    db.session.commit()

    flash(f'Your password has activated! You are now able to log in.', 'success')
    return redirect(url_for("users.login"))



@users.route("/reset_password", methods = ['POST', 'GET'])
def reset_request():
    if current_user.is_authenticated: #If user is logged in
        return redirect(url_for('main.index'))

    form = Request_Reset_Form()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        send_reset_email(user)
        flash('An email has been sent with instructions to reset your password', 'info')
        return redirect(url_for('main.index'))
    return render_template("Users/Request Reset.html", title="Reset Password", form=form)

@users.route("/reset_password/<token>", methods = ['POST', 'GET'])
def reset_token(token):
    if current_user.is_authenticated: #If user is logged in
        return redirect(url_for('main.index'))

    user = User.verify_reset_token(token)
    if user == None:
        flash('That is an invalid or expired token.', 'warning')
        return redirect(url_for('users.reset_request'))


    form = Reset_Password_Form()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8') #encryption password
        user.password = hashed_password
        db.session.commit()

        flash(f'Your password has been reset! You are now able to log in.', 'success')
        return redirect(url_for("users.login"))

    return render_template("Users/Reset Token.html", title="Reset Password", form=form)


@users.route("/Profile/History", methods = ['POST', 'GET'])
@login_required
def profile_history():
    image_files = url_for('static', filename=f"images/Profile_Picture/{current_user.image_file}")
    return render_template("Users/profile.html", title="History", image_file=image_files)



@users.route("/Profile/Edit", methods = ['POST', 'GET'])
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
        return redirect(url_for('reminder.profile_reminder'))

    elif request.method == 'GET':
        form.username.data = current_user.username
        form.email.data = current_user.email


    image_files = url_for('static', filename=f"images/Profile_Picture/{current_user.image_file}")

    return render_template("Users/profile.html", title="Edit", image_file=image_files, form=form)

