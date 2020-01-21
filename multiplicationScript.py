def run(data, parameters):
    print('parameters for this script are: ', parameters)
    data = list(map(int, data))
    returnData = data[0] * 2
    return str(returnData)
