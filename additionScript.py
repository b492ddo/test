def run(data, parameters):
    print('parameters for this script are: ', parameters)
    data = map(int, data)
    returnData = data + 10
    return str(returnData)
