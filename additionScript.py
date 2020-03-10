import json

def run(data, parameters):
    print('parameters for this script are: ', parameters)
    dictData = json.loads(data)
    dictData['data'] = str(int(dictData['data']) + 10)
    return json.dumps(dictData)
