import json

def run(data, parameters):
    listDictionaries = json.loads(data)
    minVehicleCount = int(parameters['minVehicleCount'])
    maxVehicleCount = int(parameters['maxVehicleCount'])
    print('minVehicleCount is: ' + str(minVehicleCount))
    print('maxVehicleCount is: ' + str(maxVehicleCount))

    # Filter out the elements with a vehicleCount not within the minimum and maximum
    for element in listDictionaries[:]:
        vehicleCount = getVehicleCount(element)
        print('element is: ' + str(element))
        print('vehicleCount is: ' + str(vehicleCount))
        if vehicleCount is not None:
            if (vehicleCount > maxVehicleCount) or (vehicleCount < minVehicleCount):
                print('removing')
                listDictionaries.remove(element)
            else:
                print('not removing')
                continue
        else:
            listDictionaries.remove(element)
            print('removing')
            continue

    print('number of elements is: ' + str(len(listDictionaries)))
    for element in listDictionaries:
        vehicleCount = getVehicleCount(element)
        print('vehicleCount left is: ' + str(vehicleCount))
        # Add a vehicleCount key to the data
        element['vehicleCount'] = str(vehicleCount)
    return json.dumps(listDictionaries)

def getVehicleCount(element):
    try:
        vehicleCount = int(element['properties']['count']['java.lang.Long'])
    except KeyError:
        vehicleCount = None

    # print('vehicleCount is: ' + str(vehicleCount))
    # print('type of vehicleCount is: ' + str(type(vehicleCount)))
    return vehicleCount
