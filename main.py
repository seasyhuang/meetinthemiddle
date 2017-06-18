#from googlemaps import GoogleMaps
import googlemaps
#joannas_api_key = 'AIzaSyAwpxBQ2JEdmqxf6h9IAzcOp1dFubwFoR0'
joannas_api_key = 'AIzaSyB-09W17tZ08f4mfSG4LWaqSFvuqK8MgNY'
gmaps = googlemaps.Client(key=joannas_api_key)
address = 'Constitution Ave NW & 10th St NW, Washington, DC'
loc = {u'lat': 45.501689, u'lng': -73.567256}

dict = gmaps.places_nearby(location=loc, radius = 2000, type='food')

for key in dict['results']:
    latitude = key['geometry']['location']['lat']
    longitude = key['geometry']['location']['lng']

    print key['name']+ "at at location of " + str(latitude) + ", " + str(
        longitude)

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

def main():
    happyBirthday()
    lst = [(0, 1), (2, 3)]
    # print (result)

    middlepoint(lst)

def happyBirthday():
    print ("Happy Birthday")

# lst = [(a1,a2),(b1,b2),(c1,c2),(d1,d2),(e1,e2) ]
def middlepoint( lst):
    if 2 == len(lst):
        center =((lst[0][0]+lst[1][0])/2,(lst[0][1]+lst[1][1])/2)
        print center
    if 3 == len(lst):
        center =((lst[0][0]+lst[1][0])/2,(lst[0][1]+lst[1][1])/2)
        print center


main()


#API: AIzaSyB-09W17tZ08f4mfSG4LWaqSFvuqK8MgNY


# what functions:
# apiShit() - API key
# callGoogle - query google
# optimize -  what to do with response
##### ^^^ deep learning
# what to go with data
# how to get USER data (input)
# how to visualize results
