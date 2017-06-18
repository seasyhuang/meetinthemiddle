from googleplaces import GooglePlaces, types, lang
import time
import csv

YOUR_API_KEY = 'AIzaSyB-09W17tZ08f4mfSG4LWaqSFvuqK8MgNY'

google_places = GooglePlaces(YOUR_API_KEY)

# You may prefer to use the text_search API, instead.

# If types param contains only 1 item the request to Google Places API
# will be send as type param to fullfil:
# http://googlegeodevelopers.blogspot.com.au/2016/02/changes-and-quality-improvements-in_16.html

csvfile = open('./raw.dat', 'wt')
geowriter = csv.writer(csvfile)

def print_place(q):
  for place in q.places:
      # Returned places from a query are place summaries.
      geowriter.writerow([place.geo_location['lat'], place.geo_location['lng']])
  # Are there any additional pages of results?
  time.sleep(3)
  if q.has_next_page_token:
    print_place(google_places.nearby_search(pagetoken=q.next_page_token))

def iterate_locations():
  word_list = open('./wordlist.txt', 'rt')
  with open('./neighbourhoods.dat', 'rt') as f_in:
    for location in f_in.readlines():
      for rand_query in word_list.readlines():
        query_result = google_places.nearby_search(location=location, keyword=rand_query, radius=50000)
        print_place(query_result)

iterate_locations()




