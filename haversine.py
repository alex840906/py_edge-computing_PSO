from math import radians, cos, sin, asin ,sqrt

def calc_distance(longitude1, latitude1, longitude2, latitude2):

    #convert degrees to radians
    longitude1, latitude1, longitude2, latitude2 = \
        map(radians, [longitude1, latitude1, longitude2, latitude2])

    longitude_difference = longitude2 - longitude1
    latitude1_difference = latitude2 - latitude1

    #haversine formula
    distance = sin(latitude1_difference / 2) ** 2 + \
        cos(latitude1) * cos(latitude2) * sin(longitude_difference / 2) ** 2
    distance = 2 * asin(sqrt(distance)) * 6371

    return distance