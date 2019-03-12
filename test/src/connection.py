import haversine

# for every single device, calculate the distance to each station.
# if the distance is less or equal to 35, append to the connect list
def build(station_list, device_list):
    reset_device_list(device_list)
    for device_number, each_device in enumerate(device_list):
        for station_number, each_station in enumerate(station_list):
            distance = haversine.calc_distance(each_device.longitude, each_device.latitude, \
                each_station.longitude, each_station.latitude)
            if distance <= 35:
                each_device.connect_stations.append((station_number, distance))
        each_device.connect_stations = sorted(each_device.connect_stations, key=lambda tup: tup[1])
        if each_device.connect_stations != []:
            station_list[each_device.connect_stations[0][0]].connect_devices.append((device_number, each_device.connect_stations[0][1]))
    for each_station in station_list:
        each_station.connect_devices = sorted(each_station.connect_devices, key=lambda tup: tup[1])

    # check if any station is connected by more then ten devices
    # if so, reconnect the devices to another station
    connection_over_ten = True
    while connection_over_ten == True:
        connection_over_ten = False

        for each_station in station_list:
            if len(each_station.connect_devices) > 10:
                each_station.connect_devices = sorted(each_station.connect_devices, key=lambda tup: tup[1])
                for _devices_after_tenth in range(len(each_station.connect_devices) - 10):
                    # create a function, pass each_station into the function
                    # function start###############################################################
                    device_number = each_station.connect_devices[10][0]                           #
                    each_station.remove_connection()                                              #
                    new_station_number, distance = device_list[device_number].change_connection() #
                    if new_station_number != -1:                                                  #
                        station_list[new_station_number].add_connection(device_number, distance)  #
                    # function end#################################################################

        for each_station in station_list:
            if len(each_station.connect_devices) > 10:
                connection_over_ten = True

    for each_device in device_list:
        if each_device.connect_stations != []:
            each_device.connect_stations[:] = each_device.connect_stations[0:1]

def reset_device_list(device_list):
    for each_device in device_list:
        each_device.connect_stations = []