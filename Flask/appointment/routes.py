from flask import render_template, request, Blueprint
from Flask.appointment.Postal import Postalcode
from Flask.appointment.location import *

appointment = Blueprint('appointment', __name__)

@appointment.route("/appointment.html", methods=['POST', 'GET'])
def appointments():
    title = "Appointment"

    return render_template("Appointment/appointment.html", title=title)

@appointment.route("/nearby.html", methods = ['POST', 'GET'])


def nearby():
    postal_code = request.form.get("Postal_Code")

    return render_template("Appointment/nearby.html", title="nearby", userlocation= postal_code)