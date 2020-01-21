def run(data, parameters):
    print('parameters for this script are: ', parameters)
    data = list(map(int, data))
    returnData = data + 10
    return str(returnData)
