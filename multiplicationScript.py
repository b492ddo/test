def run(data, parameters):
    print('parameters for this script are: ', parameters)
    data = map(int, data)
    returnData = data * 2
    return str(returnData)
