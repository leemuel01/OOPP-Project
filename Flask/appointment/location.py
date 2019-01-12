import requests

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
    if "opening_hours" in i and i["opening_hours"]["open_now"] == True:
        print(" is currently: open")
    elif "opening_hours" in i and i["opening_hours"]["open_now"] == False:
        print(" is currently: closed")
    else:
        print(" has no opening hours data available")
    """ 
    sql:IF EXISTS(SELECT * FROM healthlocation WHERE gmap_id=i["id"])
        UPDATE healthlocation SET gmap_name=i["name"],gmap_picture=i["icon"] WHERE gmap_id=i["id"] <--to update db from places api
        SELECT * FROM healthlocation WHERE gmap_id=i["id"] <-- select and to display row details on webpage
    """
# reset count for above loop#
simple_count = 0
