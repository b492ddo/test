from ast import literal_eval

def run(data, parameters):
    print('parameters for this script are: ', parameters)
    dictData = literal_eval(data)
    dictData['data'] = str(int(dictData['data']) * 2)
    return dictData
