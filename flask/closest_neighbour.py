"""This file will calculate the closest neighbours of a selected station"""
import math

def rad(x):
    return x * math.pi / 180 #change to radians

def find_closest_neighbours(place, neighbours):
    radius = 6378137 #Earths radius
    closest = 10000
    for location in neighbours:
        if location[0] != place[0][0]: #dont let calculate distance with itself
            dLat = rad(float(place[0][2]) - float(location[2]))  # getting the latitudes deference in rads
            dLong = rad(float(place[0][3]) - float(location[3]))  # longintude difference in rad
            a = math.sin(dLat / 2) * math.sin(dLat / 2) + math.cos(rad(float(location[2]))) * math.cos(rad(float(place[0][2]))) * math.sin(dLong / 2) * math.sin(dLong / 2)
            c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
            d = radius * c
            if d < closest: #If its closer than current closest, then change out
                closest = d
                details_neighbour = location
    print(details_neighbour)
    return details_neighbour

#####Formula taken from http://stackoverflow.com/questions/1502590/calculate-distance-between-two-points-in-google-maps-v3
# var rad = function(x) {
#   return x * Math.PI / 180;
# };
#
# var getDistance = function(p1, p2) {
#   var R = 6378137; // Earth’s mean radius in meter
#   var dLat = rad(p2.lat() - p1.lat());
#   var dLong = rad(p2.lng() - p1.lng());
#   var a = Math.sin(dLat / 2) * Math.sin(dLat / 2) +
#     Math.cos(rad(p1.lat())) * Math.cos(rad(p2.lat())) *
#     Math.sin(dLong / 2) * Math.sin(dLong / 2);
#   var c = 2 * Math.atan2(Math.sqrt(a), Math.sqrt(1 - a));
#   var d = R * c;
#   return d; // returns the distance in meter
# };