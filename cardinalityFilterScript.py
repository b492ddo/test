import json

def run(data, parameters):
    listDictionaries = json.loads(data)
    minCardinality = int(parameters['minCardinality'])
    maxCardinality = int(parameters['maxCardinality'])
    print('minCardinality is: ' + str(minCardinality))
    print('maxCardinality is: ' + str(maxCardinality))

    # Filter out the elements with a cardinality not within the minimum and maximum
    for element in listDictionaries[:]:
        cardinality = getCardinality(element)
        print('element is: ' + str(element))
        print('cardinality is: ' + str(cardinality))
        if cardinality is not None:
            if (cardinality > maxCardinality) or (cardinality < minCardinality):
                print('removing')
                listDictionaries.remove(element)
            else:
                print('not removing')
                continue
        else:
            print('not removing')
            continue

    print('number of elements is: ' + str(len(listDictionaries)))
    for element in listDictionaries:
        cardinality = getCardinality(element)
        print('cardinality left is: ' + str(cardinality))
    return json.dumps(listDictionaries)

def getCardinality(element):
    try:
        cardinality = int(element['properties']['hllp']['com.clearspring.analytics.stream.cardinality.HyperLogLogPlus']['hyperLogLogPlus']['cardinality'])
    except KeyError:
        cardinality = None

    # print('cardinality is: ' + str(cardinality))
    # print('type of cardinality is: ' + str(type(cardinality)))
    return cardinality
