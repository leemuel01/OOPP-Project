import requests
import random
from Flask.appointment.config import Config


"""
consider auto location get
Note: As of Chrome 50, the Geolocation API only works on secure contexts (HTTPS). 
If your site is hosted on a non-secure origin (such as HTTP), any requests for the user's location no longer function.

Queue watch
https://www.nup.com.sg/Pages/QueueViewer/nup_queueviewerlist.aspx
https://www.nhgp.com.sg/smile.aspx
"""


class LocationSearch(Config):
    def __init__(self,user_location_input):
        self.__location_input = user_location_input+"+singapore"
        self.__places_result = ""
        self.__result_latitude = ""
        self.__result_longitude = ""
        self.__places_nearby_hospital_result = ""
        self.__places_nearby_hospital_list = []

        super().__init__()

    def __str__(self):
        return self.__location_input

    # to overwrite super
    def read_file(self):
        try:
            api_key = open("google_maps_api_key.txt","r")
            return api_key.readline()
        except:
            # create new file, write backup api key into folder if primary key file unable to open or does not exist
            new_api_key = open("google_maps_api_key.txt","x")
            open("google_maps_api_key.txt", "w").write("AIzaSyBejFaCiDqXckcqwOo9h_VXGUeoK6ljhmo")
            backup_api_key = open("google_maps_api_key.txt", "r")
            return backup_api_key.readline()

    def run_places_api_location_input(self):
        self.__places_result = requests.get("https://maps.googleapis.com/maps/api/geocode/json?address="+self.__location_input+"&key="+self.get_api_key()+"")

    def set_result_lat_long(self):
        self.__result_latitude = str(self.__places_result.json()['results'][0]["geometry"]["location"]["lat"])
        self.__result_longitude = str(self.__places_result.json()['results'][0]["geometry"]["location"]["lng"])

    def get_result_lat_long(self):
        return "Latitude: "+ self.__result_latitude +" Longitude: "+ self.__result_longitude

    # need key word to filter as google places shows all locations that people have
    # tagged as hospital which might not be actual hospital locations
    def find_nearby_hospital(self):
        self.set_api_key()
        self.run_places_api_location_input()
        self.set_result_lat_long()
        self.__places_nearby_hospital_result = requests.get("https://maps.googleapis.com/maps/api/place/nearbysearch/json?location="
                                               + self.__result_latitude+","+self.__result_longitude
                                               + "&rankby=distance&type=hospital|doctor&keyword=general+hospital&key="
                                               + self.get_api_key())

    def nearby_hospital_update_result(self):
        database = self.database_connection()
        simple_count = 0
        for i in self.__places_nearby_hospital_result.json()["results"]:
            simple_count += 1
            # simulation of number of people in queue and urls, assuming it takes 15mins per person
            # simulate queue watch url as theres no automated way of getting those
            # to update urls manually
            simulate_queue = random.randrange(3,200)
            simulate_rooms = random.randrange(1,15)
            simulate_waiting_time = round(simulate_queue * 15 / simulate_rooms)
            simulate_appointment_url = "https://www."+i["name"].replace(" ","")+".com/appointment"
            simulate_queue_watch_url = "https://www."+i["name"].replace(" ","")+".com/queue_watch"

            # grab image from google places photo api
            if "photos" in i:
                photo_ref_0 = i["photos"][0]["photo_reference"]
                photo_ref_url = "https://maps.googleapis.com/maps/api/place/photo?maxwidth=400&photoreference="+photo_ref_0+"&key="+self.get_api_key()
            else:
                photo_ref_url = "https://upload.wikimedia.org/wikipedia/commons/a/ac/No_image_available.svg"

            # insert into database if gmap_place_id does not exist in database,
            # ignore if unique key(gmap_place_id) is found
            database.execute("INSERT OR IGNORE INTO healthlocation (gmap_place_id, gmap_name, gmap_photo, "
                             "appointment_url, queue_watch_url, current_in_queue, estimated_waiting_time, rooms) "
                             "VALUES (?,?,?,?,?,?,?,?)",(i["place_id"],i["name"],photo_ref_url,simulate_appointment_url,
                                                       simulate_queue_watch_url,simulate_queue,simulate_waiting_time,simulate_rooms))
            # update database name and photo url from places api
            database.execute("UPDATE healthlocation SET gmap_name=?,gmap_photo=? WHERE gmap_place_id=?",(i["name"],photo_ref_url,i["place_id"]))

            # append info into obj list to display
            nearby_hospital_array_loop = [simple_count,i["place_id"],i["name"],photo_ref_url,simulate_appointment_url,simulate_queue_watch_url,simulate_queue,simulate_waiting_time,simulate_rooms]
            self.__places_nearby_hospital_list.append(nearby_hospital_array_loop)
        #  need to .commit to save sql data
        database.commit()
        database.close()
        self.run_list_sql()

        """
            
            print(simple_count, i["name"], end="")
            # To check if opening_hours key available as it is not in every i object
            # and to check if its open or closed based on google places api#
            if "opening_hours" in i:
                if "open_now" in i:
                    if i["opening_hours"]["open_now"] == True:
                        print(" is currently: open")
                    elif i["opening_hours"]["open_now"] == False:
                        print(" is currently: closed")
                else:
                    print(" ")
            else:
                print(" has no opening hours data available")
            """

    def display_nearby_result(self):
        self.find_nearby_hospital()
        self.nearby_hospital_update_result()
        print(self.__places_nearby_hospital_list)
        return self.__places_nearby_hospital_list

    def run_list_sql(self):
        database = self.database_connection()
        count = 0
        for i in self.__places_nearby_hospital_list:

            place_id = i[1]
            sql_id = database.execute("SELECT id FROM healthlocation WHERE gmap_place_id = ?",(place_id,))
            for j in sql_id:
                print (j[0])
                self.__places_nearby_hospital_list[count].append(int(j[0]))
            count +=1



"""
# test
runlocationsearch = LocationSearch("400322")
runlocationsearch.display_nearby_result()
"""

"""
OLD
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
