import numpy as np
import haversine

class BaseStations():
    def __init__(self, number, longitude, latitude):
        self.number = number
        self.longitude = longitude
        self.latitude = latitude
        self.connect_devices = []

    def remove_connection(self, device_rank):
        del self.connect_devices[device_rank]

    def add_connection(self, device_number, distance):
        self.connect_devices.append((device_number, distance))

class MobileDevices():
    def __init__(self, number, longitude, latitude):
        self.number = number
        self.longitude = longitude
        self.latitude = latitude
        self.connect_stations = []

    def change_connection(self):
        if len(self.connect_stations) > 1:
            del self.connect_stations[0]
            return self.connect_stations[0][0], self.connect_stations[0][1]
        elif len(self.connect_stations) == 1:
            del self.connect_stations[0]
            return -1, 0
        else:
            return -1, 0
    
def base_station_location():
    base_station = base_station = np.loadtxt('datasets/firenze.txt', delimiter=' ')

    return base_station

def candidate_station_quantity():
    base_station = base_station_location()

    return len(base_station)

def max_longitude():
    base_station = base_station_location()
    max_longitude = base_station[:,0].max() + 0.4162376141765

    return max_longitude

def min_longitude():
    base_station = base_station_location()
    min_longitude = base_station[:,0].min() - 0.4162376141765

    return min_longitude

def max_latitude():
    base_station = base_station_location()
    max_latitude = base_station[:,1].max() + 0.3147625620716

    return max_latitude

def min_latitude():
    base_station = base_station_location()
    min_latitude = base_station[:,1].min() - 0.3147625620716

    return min_latitude

def get_diagonal():
    right_edge = max_longitude()
    left_edge = min_longitude()
    top_edge = max_latitude()
    bottom_edge = min_latitude()

    diagonal = haversine.calc_distance(right_edge, top_edge, left_edge, bottom_edge)

    return diagonal

def generate_population():
    right_edge = max_longitude()
    left_edge = min_longitude()
    top_edge = max_latitude()
    bottom_edge = min_latitude()

    population = np.zeros((2000,2))
    population[:,0] = np.random.uniform(low=left_edge, high=right_edge, size=(2000))
    population[:,1] = np.random.uniform(low=bottom_edge, high=top_edge, size=(2000))
    np.savetxt('datasets/population_firenze.txt', population, fmt="%f", newline='\n')

    return population

def generate_device_list():
    # mobile_devices = generate_population()
    mobile_devices = np.loadtxt('datasets/population_firenze.txt', delimiter=' ')
    device_list = []
    for device in range(len(mobile_devices)):
        device_list.append(MobileDevices(device, mobile_devices[device][0], mobile_devices[device][1]))
    
    return device_list

def generate_station_list(solution):
    base_station = base_station_location()
    station_list = []
    for index in range(len(base_station)):
        if solution[index] == True:
            station_list.append(BaseStations(index, base_station[index][0], base_station[index][1]))

    return station_list

def generate_distance_table():
    solution = [True] * candidate_station_quantity()
    device_list = generate_device_list()
    station_list = generate_station_list(solution)
    distance_table = []
    for each_station in station_list:
        table_element = []
        for each_device in device_list:
            table_element.append(haversine.calc_distance(each_station.longitude, each_station.latitude, each_device.longitude, each_device.latitude))
        distance_table.append(table_element[:])

    return distance_table