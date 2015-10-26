import hcl
import os

def loadConfig(path):
    name = '.loopci.hcl'
    if len([f for f in os.listdir(path) if f == name]) != 1:
        raise Exception('{0} is not found'.format(name))
    f = open(os.path.join(path, name), 'r')
    obj = hcl.load(f)
    f.close()
    return obj