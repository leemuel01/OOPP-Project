import requests
import sqlite3
from Flask.appointment.config import Config


class LocationSearch(Config):
    def __init__(self,user_location_input):
        self.__location_input = "singapore+"+user_location_input
        self.__places_result = ""
        self.__result_latitude = ""
        self.__result_longitude = ""
        self.__places_nearby_hospital_result = ""

        super().__init__()

    def __str__(self):
        return self.__location_input

    def run_places_api_location_input(self):
        self.__places_result = requests.get("https://maps.googleapis.com/maps/api/geocode/json?address="+self.__location_input+"&key="+self.get_api_key()+"")

    def set_result_lat_long(self):
        self.__result_latitude = str(self.__places_result.json()['results'][0]["geometry"]["location"]["lat"])
        self.__result_longitude = str(self.__places_result.json()['results'][0]["geometry"]["location"]["lng"])

    def get_result_lat_long(self):
        return "Latitude: "+ self.__result_latitude +" Longitude: "+ self.__result_longitude

    def find_nearby_hospital(self):
        self.set_api_key()
        self.run_places_api_location_input()
        self.set_result_lat_long()
        self.__places_nearby_hospital_result = requests.get("https://maps.googleapis.com/maps/api/place/nearbysearch/json?location="
                                               + self.__result_latitude+","+self.__result_longitude
                                               + "&rankby=distance&type=hospital&keyword=general+hospital&key="
                                               + self.get_api_key())

    def nearby_hospital_update_result(self):
        database = self.database_connection()
        simple_count = 0
        for i in self.__places_nearby_hospital_result.json()["results"]:
            simple_count += 1
            loop_place_id = i["place_id"]
            loop_name = i["name"]
            loop_photo = "test"
            print(simple_count, i["name"], end="")
            database.execute("INSERT INTO healthlocation (gmap_place_id, gmap_name, gmap_photo) VALUES (?,?,?))", (loop_place_id,loop_name,loop_photo))
            # To check if opening_hours key available as it is not in every i object
            # and to check if its open or closed based on google places api#
            if "opening_hours" in i:
                if i["opening_hours"]["open_now"] == True:
                    print(" is currently: open")
                elif i["opening_hours"]["open_now"] == False:
                    print(" is currently: closed")
            else:
                print(" has no opening hours data available")

        #  need to .commit to save sql data
        database.commit()
something = LocationSearch("400322")
something.find_nearby_hospital()
something.nearby_hospital_update_result()

"""
# connect to site.db#
sqlite_connection=sqlite3.connect("../site.db")

# user inputs location #
user_location_input = "singapore+400322"
# my google api key #
googlemaps_api_key = "AIzaSyCWLbnx9H1I-HnwzHh9kbL8PyZvYGJydiQ"
# requesting location of user input #
googlemaps_req = requests.get("https://maps.googleapis.com/maps/api/geocode/json?address="+user_location_input+"&key="+googlemaps_api_key+"")
# debug show location results#
print(googlemaps_req.json()["results"][0]["geometry"]["location"])

# user input latitude results#
googlemaps_req_latitude = str(googlemaps_req.json()['results'][0]["geometry"]["location"]["lat"])
# user input longitude results#
googlemaps_req_longitude = str(googlemaps_req.json()['results'][0]["geometry"]["location"]["lng"])
# using the previous location latitude and longitude to get nearby hospitals ranked by distance from location input#
googlemaps_req_nearby_hospital = requests.get("https://maps.googleapis.com/maps/api/place/nearbysearch/json?location="+googlemaps_req_latitude+","
                                              +googlemaps_req_longitude+
                                              "&rankby=distance&type=hospital&keyword=general+hospital&key="
                                              +googlemaps_api_key+"")
# debug show results#
print(googlemaps_req_nearby_hospital.json()["results"][4])

# loop to print results, count required as i is object itself not an int.#
simple_count = 0
for i in googlemaps_req_nearby_hospital.json()["results"]:
    simple_count+=1
    print(simple_count, i["name"],end="")
    # To check if opening_hours key available as it is not in every i object
    # and to check if its open or closed based on google places api#
    if "opening_hours" in i:
        if i["opening_hours"]["open_now"] == True:
            print(" is currently: open")
        elif i["opening_hours"]["open_now"] == False:
            print(" is currently: closed")
    else:
        print(" has no opening hours data available")
    """ """
    sql:IF EXISTS(SELECT * FROM healthlocation WHERE gmap_id=i["id"])
        UPDATE healthlocation SET gmap_name=i["name"],gmap_picture=i["icon"] WHERE gmap_id=i["id"] <--to update db from places api
        SELECT * FROM healthlocation WHERE gmap_id=i["id"] <-- select and to display row details on webpage
    """ """
# reset count for above loop#
simple_count = 0
"""
