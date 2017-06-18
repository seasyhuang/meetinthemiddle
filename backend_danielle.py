import requests



baseline_string = 'https://maps.googleapis.com/maps/api/directions/json'
joannas_api_key = 'AIzaSyAwpxBQ2JEdmqxf6h9IAzcOp1dFubwFoR0'
def execute_google_api_call(origin_gps, destination_gps, api_key):
    origin_lattitude, origin_longitude = origin_gps
    destination_lattitude, destination_longitude = destination_gps
    api_call = baseline_string + '?' + 'origin=' + origin_lattitude + ',' + origin_longitude + "&" + 'desination=' + destination_lattitude + ',' + destination_longitude + '&' + 'key=' + api_key
    response = requests.get(api_call)
    print(response)


execute_google_api_call(())