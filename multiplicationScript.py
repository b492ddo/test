import json

def run(data, parameters):
    print('parameters for this script are: ', parameters)
    dictData = json.loads(data)
    dictData['testKey'] = str(int(dictData['testKey']) * 2)
    return dictData
