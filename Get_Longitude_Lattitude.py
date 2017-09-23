#!/usr/bin/python3
# The urllib2 module has been split across several modules in Python 3 named urllib.request and urllib.error
from urllib.request import urlopen
import json, time

def GetGeoCode(Address, API_KEY=""):
	# https://developers.google.com/maps/documentation/geocoding/start
	BaseURL = r"https://maps.googleapis.com/maps/api/geocode/json?"

	Address_Parameter = "address=" + Address.replace(" ", "+")
	print ("Address_Parameter: " + Address_Parameter)

	FinalURL = BaseURL + Address_Parameter + "&key=" + API_KEY 
	print ("FinalURL: " + FinalURL)

	HTMLResponse = urlopen(FinalURL)
	JSONRaw = HTMLResponse.read().decode('utf8')

	print ("============== JSONRaw =============")
	print (JSONRaw)

	JSONData = json.loads(JSONRaw)
	print ("============== JSONData =============")
	print (JSONData)

	GeoCodeList = []
	if JSONData['status'] == 'OK':
		QueryResult = JSONData['results'][0]
		GeoCodeList = [ QueryResult['formatted_address'], QueryResult['geometry']['location']['lat'], QueryResult['geometry']['location']['lng']]

	#time.sleep(2)

	return GeoCodeList

Postal_Address = "155 Lambert Dr, Princeton, NJ, United States"

GeoCodeList = GetGeoCode(Address=Postal_Address)
print (GeoCodeList)

# Ref: https://developers.google.com/maps/documentation/geocoding/start
# Ref: https://andrewpwheeler.wordpress.com/2016/04/05/using-the-google-geocoding-api-with-python/

# ====================== Output ==================== #

# Address_Parameter: address=155+Lambert+Dr,+Princeton,+NJ,+United+States
# FinalURL: https://maps.googleapis.com/maps/api/geocode/json?address=155+Lambert+Dr,+Princeton,+NJ,+United+States&key=
# ============== JSONRaw =============
# {
#    "results" : [
#       {
#          "address_components" : [
#             {
#                "long_name" : "155",
#                "short_name" : "155",
#                "types" : [ "street_number" ]
#             },
#             {
#                "long_name" : "Lambert Drive",
#                "short_name" : "Lambert Dr",
#                "types" : [ "route" ]
#             },
#             {
#                "long_name" : "Princeton",
#                "short_name" : "Princeton",
#                "types" : [ "locality", "political" ]
#             },
#             {
#                "long_name" : "Mercer County",
#                "short_name" : "Mercer County",
#                "types" : [ "administrative_area_level_2", "political" ]
#             },
#             {
#                "long_name" : "New Jersey",
#                "short_name" : "NJ",
#                "types" : [ "administrative_area_level_1", "political" ]
#             },
#             {
#                "long_name" : "United States",
#                "short_name" : "US",
#                "types" : [ "country", "political" ]
#             },
#             {
#                "long_name" : "08540",
#                "short_name" : "08540",
#                "types" : [ "postal_code" ]
#             },
#             {
#                "long_name" : "2306",
#                "short_name" : "2306",
#                "types" : [ "postal_code_suffix" ]
#             }
#          ],
#          "formatted_address" : "155 Lambert Dr, Princeton, NJ 08540, USA",
#          "geometry" : {
#             "bounds" : {
#                "northeast" : {
#                   "lat" : 40.3409686,
#                   "lng" : -74.6968112
#                },
#                "southwest" : {
#                   "lat" : 40.3407603,
#                   "lng" : -74.6971631
#                }
#             },
#             "location" : {
#                "lat" : 40.3408644,
#                "lng" : -74.6969871
#             },
#             "location_type" : "ROOFTOP",
#             "viewport" : {
#                "northeast" : {
#                   "lat" : 40.34221343029149,
#                   "lng" : -74.6956381697085
#                },
#                "southwest" : {
#                   "lat" : 40.33951546970849,
#                   "lng" : -74.69833613029151
#                }
#             }
#          },
#          "place_id" : "ChIJqwBmSAbkw4kRSvhnD8cWWyw",
#          "types" : [ "premise" ]
#       }
#    ],
#    "status" : "OK"
# }
# 
# ============== JSONData =============
# {'status': 'OK', 'results': [{'types': ['premise'], 'address_components': [{'short_name': '155', 'types': ['street_number'], 'long_name': '155'}, {'short_name': 'Lambert Dr', 'types': ['route'], 'long_name': 'Lambert Drive'}, {'short_name': 'Princeton', 'types': ['locality', 'political'], 'long_name': 'Princeton'}, {'short_name': 'Mercer County', 'types': ['administrative_area_level_2', 'political'], 'long_name': 'Mercer County'}, {'short_name': 'NJ', 'types': ['administrative_area_level_1', 'political'], 'long_name': 'New Jersey'}, {'short_name': 'US', 'types': ['country', 'political'], 'long_name': 'United States'}, {'short_name': '08540', 'types': ['postal_code'], 'long_name': '08540'}, {'short_name': '2306', 'types': ['postal_code_suffix'], 'long_name': '2306'}], 'formatted_address': '155 Lambert Dr, Princeton, NJ 08540, USA', 'place_id': 'ChIJqwBmSAbkw4kRSvhnD8cWWyw', 'geometry': {'location': {'lng': -74.6969871, 'lat': 40.3408644}, 'location_type': 'ROOFTOP', 'bounds': {'southwest': {'lng': -74.6971631, 'lat': 40.3407603}, 'northeast': {'lng': -74.6968112, 'lat': 40.3409686}}, 'viewport': {'southwest': {'lng': -74.69833613029151, 'lat': 40.33951546970849}, 'northeast': {'lng': -74.6956381697085, 'lat': 40.34221343029149}}}}]}
# ['155 Lambert Dr, Princeton, NJ 08540, USA', 40.3408644, -74.6969871]
