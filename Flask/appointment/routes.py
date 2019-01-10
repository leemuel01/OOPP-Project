from flask import render_template, request, Blueprint

from Flask.appointment.Postal import Postalcode

appointment = Blueprint('appointment', __name__)

@appointment.route("/appointment.html", methods=['POST', 'GET'])
def appointments():
    title = "Appointment"

    return render_template("Appointment/appointment.html", title=title)

@appointment.route("/nearby.html", methods = ['POST', 'GET'])
def nearby():

    objuserpostal = Postalcode(request.form['postalcode'])

    return render_template("Appointment/nearby.html",userlocation=objuserpostal.generallocation())