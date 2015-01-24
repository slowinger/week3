# Divvy Bike problem
# Week3 Assignment
#By: Stephen Lowinger

import json
from math import sqrt
from urllib.request import urlopen

webservice_url = "http://www.divvybikes.com/stations/json"
data = urlopen(webservice_url).read().decode("utf8")
result = json.loads(data)
stations = result['stationBeanList']

young_latitude = 41.793414
young_longitude = -87.600915

distance = float(999999999)
for station in stations:
    station_latitude = station['latitude']
    station_longitude = station['longitude']
    station_name = station['stationName']
    station_available_docks = station['availableDocks']
    station_total_docks = station['totalDocks']

    new_distance = sqrt((station_latitude - young_latitude)**2 + (station_longitude - young_longitude)**2)
    if new_distance < distance:
        distance = new_distance
        closest_station = station_name
        closest_station_available_docks = station_available_docks
        closest_station_total_docks = station_total_docks
        closest_available_bikes = closest_station_total_docks - closest_station_available_docks
print(
    "The nearest station is: %s\nThe station has %s available bikes"
    % (closest_station, closest_available_bikes))

