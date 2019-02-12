import numpy as np
import haversine

class BaseStations():
    def __init__(self, longitude, latitude):
        self.longitude = longitude
        self.latitude = latitude
        self.connect_devices = []

    def remove_connection(self):
        del self.connect_devices[10]

    def add_connection(self, device_number, distance):
        self.connect_devices.append((device_number, distance))

class MobileDevices():
    def __init__(self, longitude, latitude):
        self.longitude = longitude
        self.latitude = latitude
        self.connect_stations = []

    def change_connection(self):
        del self.connect_stations[0]
        if len(self.connect_stations) != 0:
            return self.connect_stations[0][0], self.connect_stations[0][1]
        else:
            return -1, 0
    
def base_station_location():
    base_station = base_station = np.loadtxt('py_edge-computing_PSO/datasets/mcc283.txt', delimiter=' ')

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

    population = np.zeros((1000,2))
    population[:,0] = np.random.uniform(low=left_edge, high=right_edge, size=(1000))
    population[:,1] = np.random.uniform(low=bottom_edge, high=top_edge, size=(1000))
    np.savetxt("py_edge-computing_PSO/datasets/population.txt", population, fmt="%f", newline='\n')

    return population

def generate_device_list():
    # mobile_devices = generate_population()
    mobile_devices = np.loadtxt("py_edge-computing_PSO/datasets/population.txt", delimiter=' ')
    device_list = []
    for device in range(len(mobile_devices)):
        device_list.append(MobileDevices(mobile_devices[device][0], mobile_devices[device][1]))
    
    return device_list

def generate_station_list(solution):
    base_station = base_station_location()
    station_list = []
    for index in range(len(base_station)):
        if solution[index] == True:
            station_list.append(BaseStations(base_station[index][0], base_station[index][1]))

    return station_list