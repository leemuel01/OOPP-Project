from flask import Flask
from flask_sqlalchemy import SQLAlchemy #database stuff
from flask_bcrypt import Bcrypt #password encryption stuff
from flask_login import LoginManager #Login stuff
from flask_mail import Mail
from Flask.config import Config

#Database
db = SQLAlchemy()
#Password encryption
bcrypt = Bcrypt()
#Login management
login_manager = LoginManager()
#Login required
login_manager.login_view = 'users.users'
login_manager.login_message_category = 'info'


mail = Mail()


#Recommender by the Flask docs
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
    app.register_blueprint(errors)

    return app