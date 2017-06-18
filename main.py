#!/usr/bin/python

#from googlemaps import GoogleMaps
# Anaelle
import googlemaps
import urllib, json
import pprint
import sys

# from apiclient.discovery import build # need to download this with sudo pip install --upgrade google-api-python-client

#Derek
import time
import urllib2

#joannas_api_key = 'AIzaSyAwpxBQ2JEdmqxf6h9IAzcOp1dFubwFoR0'
joannas_api_key = 'AIzaSyB-09W17tZ08f4mfSG4LWaqSFvuqK8MgNY'
gmaps = googlemaps.Client(key=joannas_api_key)
address = 'Constitution Ave NW & 10th St NW, Washington, DC'
loc = {u'lat': 45.501689, u'lng': -73.567256}

dict = gmaps.places_nearby(location=loc, radius = 2000, type='parking')

for key in dict['results']:
    latitude = key['geometry']['location']['lat']
    longitude = key['geometry']['location']['lng']

    print key['name']+ " at location of " + str(latitude) + ", " + str(
        longitude)+'at distance '
#
# amusement_park accounting airport aquarium art_gallery atm bakery bank bar beauty_salon bicycle_store book_store
# bowling_alley bus_station cafe campground car_dealer car_rental car_repair car_wash casino cemetery church city_hall
# clothing_store convenience_store courthouse dentist department_store doctor electrician electronics_store embassy
# establishment  finance  fire_station florist food  funeral_home furniture_store
# gas_station general_contractor  grocery_or_supermarket  gym hair_care hardware_store health 
# hindu_temple home_goods_store hospital insurance_agency jewelry_store laundry lawyer library liquor_store local_government_office
# locksmith lodging meal_delivery meal_takeaway mosque movie_rental movie_theater moving_company museum night_club painter park
# parking pet_store pharmacy physiotherapist place_of_worship  plumber police post_office real_estate_agency restaurant
# roofing_contractor rv_park school shoe_store shopping_mall spa stadium storage store subway_station synagogue taxi_stand
# train_station transit_station travel_agency university veterinary_care zoo
#
# print (dict)
# lat, lng = gmaps.address_to_latlng(address)
# print lat, lng
# 38.8921021 -77.0260358
# Reverse Geocoding: find the nearest address to (lat, lng)

# destination = gmaps.latlng_to_address(38.887563, -77.019929)
# print destination
# Independence and 6th SW, Washington, DC 20024, USA
# Local Search: find places matching a query near a given location

# local = gmaps.local_search('cafe near ' + destination)
# print local['responseData']['results'][0]['titleNoFormatting']
# Vie De France Bakery & Cafe



API_KEY = "AIzaSyB-09W17tZ08f4mfSG4LWaqSFvuqK8MgNY"

def main():
    # moveMidpoint(111, 2222, 333333)
    test_origin = "75 9th Ave New York, NY"
    test_origin2 = "75 10th Ave New York, NY"
    test_origin3 = "75 11th Ave New York, NY"
    test_destination = "1124 Robie St Halifax, NS"

    print distanceMatrix(test_origin, test_origin2, test_origin3, test_destination)

    # print queryDistance(test_origin, test_destination)


# def simpleAPI():
#     api_key = "AIzaSyB-09W17tZ08f4mfSG4LWaqSFvuqK8MgNY" # <-- our API key
#     service = build('books', 'v1', developerKey=api_key)
#     request = service.volumes().list(source='public', q='android')
#     response = request.execute()
#     pprint.pprint(response)
#
#     print 'Found %d books:' % len(response['items'])
#     for book in response.get('items', []):
#         print 'Title: %s, Authors: %s' % (
#             book['volumeInfo']['title'],
#             book['volumeInfo']['authors'])

# optimization: changing the midpoint
# input: three times from three locations x1, x2, x3,
def moveMidpoint(t1, t2, t3):
    # input 3 times: check to see which one is largest
    times = [t1, t2, t3]
    largestTime = max(times) # --> want to move the midpoint toward respective person

# TEMPLATE : https://maps.googleapis.com/maps/api/distancematrix/json?origins=ORIGIN&destinations=DESTINATION&departure_time=TIME.NOW&traffic_model=best_guess&key=YOUR_API_KEY

def generateTravelTimeRequestURL(origin, destination):
    origin = origin.replace(" ", "+")
    destination = destination.replace(" ", "+")
    departure_time = int(time.time())

    site = "https://maps.googleapis.com/maps/api/distancematrix/json?origins=%s&destinations=%s&departure_time=%s&traffic_model=best_guess&key=%s" % (origin, destination, departure_time, API_KEY)

    return site

def queryDistance(origin, destination):
    request = urllib2.Request(generateTravelTimeRequestURL(origin, destination))
    response = urllib2.urlopen(request)
    json_data  = json.loads(response.read())
    relevant_data = json_data["rows"][0]["elements"][0]
    distance = relevant_data["distance"]["value"] # meters
    duration_in_traffic = relevant_data["duration_in_traffic"]["value"] # seconds

    return distance, duration_in_traffic

def distanceMatrix(person1, person2, person3, initialMidpoint):
    people = [person1, person2, person3]

    distances = []
    duration_in_traffic_times = []

    for person in people:
        distance, duration_in_traffic = queryDistance(person, initialMidpoint)
        distances.append(distance)
        duration_in_traffic_times.append(duration_in_traffic)

    return distances, duration_in_traffic_times


main()




# what functions:
# apiShit() - API key
# callGoogle - query google
# optimize -  what to do with response from API
##### ^^^ deep learning
# what to go with data
# how to get USER data (input)
# how to visualize results
