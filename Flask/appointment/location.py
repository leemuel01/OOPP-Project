import requests

user_location_input = "singapore+400322"
googlemaps_api_key = "AIzaSyCWLbnx9H1I-HnwzHh9kbL8PyZvYGJydiQ"
googlemaps_req = requests.get("https://maps.googleapis.com/maps/api/geocode/json?address="+user_location_input+"&key="+googlemaps_api_key+"")
print(googlemaps_req.json()["results"][0]["geometry"]["location"])

googlemaps_req_latitude = googlemaps_req.json()['results'][0]["geometry"]["location"]["lat"]
googlemaps_req_longitude = googlemaps_req.json()['results'][0]["geometry"]["location"]["lng"]

googlemaps_req_nearby_hospital = requests.get("https://maps.googleapis.com/maps/api/place/nearbysearch/json?location="+str(googlemaps_req_latitude)+","+str(googlemaps_req_longitude)+"&radius=15000&type=hospital&keyword=general+hospital&key="+googlemaps_api_key+"")

print(googlemaps_req_nearby_hospital.json()["results"][0])

simple_count = 0
for i in googlemaps_req_nearby_hospital.json()["results"]:
    simple_count+=1
    print(simple_count, i["name"])

simple_count = 0