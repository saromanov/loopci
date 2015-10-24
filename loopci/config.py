import pyhcl
import os

def loadConfig(path):
    name = '.loopci.hcl'
    if len([f for f in os.listdir(path) if f == name]) != 1:
        raise Exception('{0} is not found', name)
    f = open(os.path.join(path, name), 'r')
    obj = pyhcl.hcl.load(f.read())
    f.close()
    return obj