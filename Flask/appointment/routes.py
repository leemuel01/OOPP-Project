from flask import render_template, request, Blueprint
from Flask.appointment.location import LocationSearch


appointment = Blueprint('appointment', __name__)

@appointment.route("/appointment.html", methods=['POST', 'GET'])
def appointments():
    title = "Appointment"

    return render_template("Appointment/appointment.html", title=title)

@appointment.route("/nearby.html", methods = ['POST', 'GET'])


def nearby():
    postal_code = request.form.get("Postal_Code")
    test4 = LocationSearch(postal_code)
    test4.display_nearby_result()

    return render_template("Appointment/nearby.html", title="nearby", display_result_list= test4.display_nearby_result())