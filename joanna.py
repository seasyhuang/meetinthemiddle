import googlemaps

# setup
seasys_api_key = 'AIzaSyB-09W17tZ08f4mfSG4LWaqSFvuqK8MgNY'
gmaps = googlemaps.Client(key=seasys_api_key)

# input
location1 = (45.5067671, -73.56373980000001) # Desjardins Lab
location2 = (45.4795202, -73.57696529999998) # Atwater
midpoint = (45.493144, -73.570354)

# compute trip time
distanceMatrix = gmaps.distance_matrix(location1, midpoint)
duration = distanceMatrix['rows'][0]['elements'][0]['duration']['value'] # time in seconds

print(duration)



