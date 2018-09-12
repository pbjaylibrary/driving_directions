import googlemaps
from datetime import datetime
import json

def optimal_route(**kwargs):
    
    gmaps = googlemaps.Client(key=google_api_key)

    new_stop = []
    for stop in kwargs['stops']:
        new_stop.append(str(stop).replace('\'',"").replace('(','\"').replace(')','\"'))
    
    directions_result = gmaps.directions(kwargs['start'],
                                         kwargs['finish'],
                                         mode="driving",
                                         waypoints=[stop for stop in new_stop],
                                         departure_time=kwargs['departure_time'], 
                                         optimize_waypoints=True)

    return directions_result

####################################################################################
#example

google_api_key = 'insert your key here'

departure_time = datetime.now()

my_kwargs = { 
    'start':"350 5th Ave, New York, NY 10118",
    'finish':"405 Lexington Avenue, New York, NY 10174",
    'stops':["620 Eighth Avenue, New York 10018","11 Wall Street, New York, NY"],
    'departure_time':departure_time,
    'api_key':google_api_key,
}

test = optimal_route(**my_kwargs)
print (json.dumps(test, indent=4))
