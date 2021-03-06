from flask import render_template, request, Blueprint
from Flask.appointment.location import LocationSearch
from Flask.appointment.config import Config

appointment = Blueprint('appointment', __name__)

@appointment.route("/appointment.html", methods=['POST', 'GET'])
def appointments():
    title = "Appointment"

    return render_template("Appointment/appointment.html", title=title)

@appointment.route("/nearby.html", methods = ['POST', 'GET'])
def nearby():
    postal_code = request.form.get("Postal_Code")
    nearby = LocationSearch(postal_code)
    nearby.display_nearby_result()

    return render_template("Appointment/nearby.html", title="nearby", display_result_list= nearby.display_nearby_result())

@appointment.route("/locations/<location_id>",methods = ['POST', 'GET'])
def locations(location_id):
    location_config = Config()
    database = location_config.database_connection()
    location_information = database.execute("SELECT * FROM healthlocation WHERE id = ?",(location_id,))
    location_config.set_api_key()
    api_key = location_config.get_api_key()

    return render_template("Appointment/location.html", display_location_info = location_information, api_key_loc=api_key)

@appointment.route("/all_location",methods = ['POST', 'GET'])
def all_location():
    all_location_config = Config()
    database = all_location_config.database_connection()
    all_location_information = database.execute("SELECT * FROM healthlocation")


    return render_template("Appointment/all_location.html", display_all_location=all_location_information)
