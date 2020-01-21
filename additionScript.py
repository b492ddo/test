def run(data, parameters):
    print('parameters for this script are: ', parameters)
    data = list(map(int, data))
    print(data)
    returnData = data + 10
    return str(returnData)
