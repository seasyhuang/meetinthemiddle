#!/usr/bin/python
import urllib, json
import pprint
import sys
from apiclient.discovery import build #need to download this with sudo pip install --upgrade google-api-python-client

def main():
    simpleAPI()

def simpleAPI():
    api_key = "AIzaSyB-09W17tZ08f4mfSG4LWaqSFvuqK8MgNY"
    service = build('books', 'v1', developerKey=api_key)
    request = service.volumes().list(source='public', q='android')
    response = request.execute()
    pprint.pprint(response)

    print 'Found %d books:' % len(response['items'])
    for book in response.get('items', []):
        print 'Title: %s, Authors: %s' % (
            book['volumeInfo']['title'],
            book['volumeInfo']['authors'])

main()


#API: AIzaSyB-09W17tZ08f4mfSG4LWaqSFvuqK8MgNY


# what functions:
# apiShit() - API key
# callGoogle - query google
# optimize -  what to do with response from API
##### ^^^ deep learning
# what to go with data
# how to get USER data (input)
# how to visualize results

#Functions to grab the necessary data from Google.

# #Grabbing and parsing the JSON data
# def GoogPlac(lat,lng,radius,types,key):
#   #making the url
#   AUTH_KEY = key
#   LOCATION = str(lat) + "," + str(lng)
#   RADIUS = radius
#   TYPES = types
#   MyUrl = ('https://maps.googleapis.com/maps/api/place/nearbysearch/json'
#            '?location=%s'
#            '&radius=%s'
#            '&types=%s'
#            '&sensor=false&key=%s') % (LOCATION, RADIUS, TYPES, AUTH_KEY)
#   #grabbing the JSON result
#   response = urllib.urlopen(MyUrl)
#   jsonRaw = response.read()
#   jsonData = json.loads(jsonRaw)
#   return jsonData
#
# #This is a helper to grab the Json data that I want in a list
# def IterJson(place):
#   x = [place['name'], place['reference'], place['geometry']['location']['lat'],
#          place['geometry']['location']['lng'], place['vicinity']]
#   return x
