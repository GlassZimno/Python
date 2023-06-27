#Glass Zimno
#24/6/2023

import googlemaps

gmaps = googlemaps.Client(key='AIzaSyDL9xYyxzjYsy-P6tOaVipaNA7KrgWtHIM')
destinations = []
while 1:
  inp = input("Add destination: ")
  if inp == "":
    break
  destinations.append(inp + " UK")

distances = gmaps.distance_matrix("Hull UK", destinations, "transit")
print(distances["rows"]["elements"][0]["duration"]["value"])

{
  'destination_addresses': ['Liverpool, UK',
                            'Manchester, UK'],
 'origin_addresses': ['Hull, UK'],
 'rows': [{
   'elements': [{
     'distance': {
       'text': '215 km',
       'value': 215219
       },
     'duration': {
       'text': '4 hours 34 mins',
       'value': 16440
       },
     'status': 'OK'
     },
                {
                  'distance': {
                    'text': '164 km',
                    'value': 163847
                    },
                  'duration': {
                    'text': '3 hours 37 mins',
                    'value': 13020
                    }, 'status': 'OK'
                  }]
   }],
  'status': 'OK'
  }

