import hcl
import os

def loadConfig(path):
    name = '.loopci.hcl'
    if len([f for f in os.listdir(path) if f == name]) != 1:
        raise Exception('{0} is not found'.format(name))
    f = open(os.path.join(path, name), 'r')
    obj = hcl.load(f)
    print(obj)
    f.close()
    return obj

def loadJSONConfig(path):
    ''' optional. load config in json format
    '''
    name = '.loopci.json'
    if len([f for f in os.listdir(path) if f == name]) != 1:
        raise Exception('{0} is not found'.format(name))
    f = open(os.path.join(path, name), 'r')
    obj = json.loads(f.read())
    f.close()
    return obj