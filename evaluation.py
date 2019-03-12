import dataset
import connection

def calc_latency(device_list):
   latency = 0
   maximum = 0
   minimum = dataset.get_diagonal()
   normalization = 0
   quantity = 0

   for each_device in device_list:
       if each_device.connect_stations != []:
           # latency += each_device.connect_stations[1]
           if (1 / each_device.connect_stations[0][1]) > maximum:
               maximum = (1 / each_device.connect_stations[0][1])
           elif (1 / each_device.connect_stations[0][1]) < minimum:
               minimum = (1 / each_device.connect_stations[0][1])
       quantity += 1
   for each_device in device_list:
       if each_device.connect_stations != []:
           normalization += ((1 / each_device.connect_stations[0][1]) - minimum) / (maximum - minimum)
   latency = normalization / quantity

   return latency

def calc_cost(station_list):
   cost = 0
   for _each_station in station_list:
       cost += 1
   quantity = dataset.candidate_station_quantity()
   if cost == 0:
       return 1
   else:
       cost = ((1 / cost) - (1 / quantity)) / (1 - (1 / quantity))
       return cost

def calc_utilization(station_list):
   station_quantity = 0
   connected_stations = 0
   for each_station in station_list:
       station_quantity += 1
       if each_station.connect_devices != []:
           connected_stations += 1
   if station_quantity == 0:
       return 0
   else:
       utilization = connected_stations / station_quantity
       return utilization

def calc_experience(device_list):
   device_quantity = 0
   connected_devices = 0
   for each_device in device_list:
       device_quantity += 1
       if each_device.connect_stations != []:
           connected_devices += 1
   experience = connected_devices / device_quantity

   return experience

def evaluate(solution, device_list):
   station_list = dataset.generate_station_list(solution)
   connection.build(station_list, device_list)
   latency = calc_latency(device_list)
   cost = calc_cost(station_list)
   utilization = calc_utilization(station_list)
   experience = calc_experience(device_list)

   return (latency * cost * utilization * experience)