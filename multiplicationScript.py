def run(data, parameters):
    print('parameters for this script are: ', parameters)
    results = list(map(int, data))
    returnData = results * 2
    return str(returnData)
