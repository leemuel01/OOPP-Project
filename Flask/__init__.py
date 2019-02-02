from datetime import datetime, timedelta

from flask import Flask
from flask_sqlalchemy import SQLAlchemy #database stuff
from flask_bcrypt import Bcrypt #password encryption stuff
from flask_login import LoginManager #Login stuff
from flask_mail import Mail


from Flask.config import Config
from Flask.reminder.functions import send_whatsapp_msg

import threading
import atexit

#threading
POOL_TIME = 5
# dataLock = threading.Lock() # lock to control access to variable
reminder_thread = threading.Thread() # thread handler


db = SQLAlchemy() #Database
bcrypt = Bcrypt() #Password encryption
login_manager = LoginManager() #Login management
login_manager.login_view = 'users.users' #Login required
login_manager.login_message_category = 'info' #Login info
mail = Mail() #Flaskmail


#Recommender by the Flask docs http://flask.pocoo.org/docs/1.0/patterns/appfactories/
#Also for Blueprints
def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(Config)


    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)
    mail.init_app(app)

    from Flask.appointment.routes import appointment
    from Flask.feedback.routes import feedback
    from Flask.main.routes import main
    from Flask.medical_history.routes import medical_history
    from Flask.medical_teacher.routes import medical_teacher
    from Flask.symptom_checker.routes import symptom_checker
    from Flask.trivia.routes import trivia
    from Flask.users.routes import users
    from Flask.reminder.routes import reminder
    from Flask.errors.handlers import errors

    app.register_blueprint(appointment)
    app.register_blueprint(feedback)
    app.register_blueprint(main)
    app.register_blueprint(feedback)
    app.register_blueprint(medical_history)
    app.register_blueprint(medical_teacher)
    app.register_blueprint(symptom_checker)
    app.register_blueprint(trivia)
    app.register_blueprint(users)
    app.register_blueprint(reminder)
    app.register_blueprint(errors)

    #creates database if none
    with app.app_context():
        db.create_all()

    #threading stuff

    #stops thread
    def interrupt():
        global reminder_thread
        reminder_thread.cancel()

    def doStuff():
        global reminder_thread
        with app.app_context(): #sets the app context
            from Flask.Models import Reminders
            try:
                reminders = Reminders.query.order_by(Reminders.date).first()
                remind_time = reminders.date - timedelta(hours=2)

            except AttributeError:
                pass
            else:
                print(remind_time)

                if remind_time <= datetime.now():
                    send_whatsapp_msg(reminders.reminder, reminders.date)
                    db.session.delete(reminders)
                    db.session.commit()




        # Set the next thread to happen
        reminder_thread = threading.Timer(POOL_TIME, doStuff, ())
        reminder_thread.start()

    def Reminder_Thread_Start():
        global reminder_thread
        #Thread creation
        reminder_thread = threading.Timer(POOL_TIME, doStuff, ())
        reminder_thread.start()

    # Initiate
    Reminder_Thread_Start()
    # When you kill Flask (SIGTERM), clear the trigger for the next thread
    atexit.register(interrupt)
    return app