"""This file will calculate the closest neighbours of a selected station"""
import math

def rad(x):
    return x * math.pi / 180 #change to radians

def find_closest_neighbours(place, neighbours):
    radius = 6378137 #Earths radius
    details_neighbour = [neighbours[0], neighbours[1], neighbours[2]]
    closest1 = 10000
    closest2 = 10001
    closest3 = 10002
    for location in neighbours:
        if location[0] != place[0][0]: #dont let calculate distance with itself
            dLat = rad(float(place[0][2]) - float(location[2]))  # getting the latitudes deference in rads
            dLong = rad(float(place[0][3]) - float(location[3]))  # longintude difference in rad
            a = math.sin(dLat / 2) * math.sin(dLat / 2) + math.cos(rad(float(location[2]))) * math.cos(rad(float(place[0][2]))) * math.sin(dLong / 2) * math.sin(dLong / 2)
            c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
            d = radius * c
            if d < closest1: #If its closer than current closest, then change out
                closest3 = closest2
                closest2 = closest1
                closest1 = d
                details_neighbour[2] = details_neighbour[1]
                details_neighbour[1] = details_neighbour[0]
                details_neighbour[0] = location
            elif d < closest2:
                closest3 = closest2
                closest2 = d
                details_neighbour[2] = details_neighbour[1]
                details_neighbour[1] = location
            elif d < closest3:
                closest3 = d
                details_neighbour[2] = location
    
    for i in range(3):
        details_neighbour[i] = list(details_neighbour[i])
        var = details_neighbour[i][1]
        details_neighbour[i][1] = var.lower()
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