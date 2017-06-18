#!/usr/bin/python

# Anaelle
# import googlemaps
import json
import pprint
import sys

# Derek
import time #time.now
import urllib2 #HTTP requests
import re #regex
import math
import numpy
import random

# Global Constants
API_KEY = "AIzaSyB-09W17tZ08f4mfSG4LWaqSFvuqK8MgNY"
DISTANCE_TRAVELLED_IN_10_MINUTES = 833
DAT_FILE = "scrape_stuff/raw.dat"
MAX_LABELS = 100

# ------------------------------------------------- DATA CALL ---------------------------------------------

#CALL THIS
def create_label_with_points():
    # returns array of size 100
    file = open_dat_file()

    data = numpy.array

    count = 0
    for midpoints in file:

        numpy.append(data, generate_element_in_row(midpoints))

        count++
        break if count >= MAX_LABELS

    return data

# ------------------------------------------------- MIDPOINT CALCULATION ---------------------------------------------

def generateTravelTimeRequestURL(origin, destination):

    if not is_address(origin): # returns true if address is in coordinates
        origin = address_to_string(origin)
        destination = address_to_string(destination)

    departure_time = int(time.time())

    site = "https://maps.googleapis.com/maps/api/distancematrix/json?origins=%s&destinations=%s&departure_time=%s&traffic_model=best_guess&key=%s" % (origin, destination, departure_time, API_KEY)

    return site

def address_to_string(address):
    return address.replace(" ", "+")

def is_address(location):
    if re.match("(-)?\d+\.\d+.(-)?\d+\.\d+", location):
        True
    else:
        False

def queryDistance(origin, destination):
    json_data = send_url(generateTravelTimeRequestURL(origin, destination))
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

# -------------------------------------------------- WEB CALLS -----------------------------------------

def send_url(site):
    request = urllib2.Request(site)
    response = urllib2.urlopen(request)
    json_data  = json.loads(response.read())

    return json_data

# -------------------------------------------------- CALCULATING DATA POINTS -----------------------------------------

def calculate_data_point_x(x1, y1, x2, y2):
    theta = calculate_degrees(x1, y1, x2, y2)
    data_point_x_x_coordinate = DISTANCE_TRAVELLED_IN_10_MINUTES*math.cos(theta)
    data_point_x_y_coordinate = DISTANCE_TRAVELLED_IN_10_MINUTES*math.sin(theta)

    return data_point_x_x_coordinate, data_point_x_y_coordinate

def calculate_degrees(x1, y1, x2, y2):
    return math.atan((x2 - x1)/(y2 - y1))

# ------------------------------------------------- ACCESSING DATA --------------------------------------------------

def random_points():
    file = open_dat_file()
    arry_length = len(file)

    random_coordinates = []

    for i in range(2):
        random_coordinates.append(random.randrange(arry_length))

    return random_points

def open_dat_file():
    return numpy.fromfile(DAT_FILE,dtype=float)

# ------------------------------------------------- CREATING LABEL ARRAY ---------------------------------------------

def generate_element_in_row(midpoint):
    # takes the form = [(label_x, label_y), (rand_x1, rand_y1), (rand_x2, rand_y2), (rand_x3, rand_y3)]
    label_x, label_y = find_x_y(midpoint)
    points = triple_points(midpoint)

    return [(label_x, label_y), points[0], points[1], points[2]]

def find_x_y(coordinate):
    stripped_coordinate = [x.strip() for x in coordinate.split(',')]
    return stripped_coordinate[0], stripped_coordinate[1] #x, y

def triple_points(midpoint):
    triple_x = []

    for i in range(2):
        rand_x, rand_y = find_x_y(random_points())
        mid_x, mid_y = find_x_y(midpoints)
        x_x, x_y = calculate_data_point_x(mid_x, mid_y, rand_x, rand_y)
        triple_x.append((x_x, x_y))

    return triple_x
