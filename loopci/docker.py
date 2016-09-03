import os
import sh
import random
import string

#TODO. Need to use Docker client

class DockerManager:
    ''' This class provides all about management with docker
        This class starts after construction of Dockerfile
    '''
    def __init__(self, *args, **kwargs):
        self.config = kwargs.get('config')

    def cp(self, path, contname):
         dockercp = sh.Command('docker')
         dockercp('cp', path, contname + ':/dir1')


    def build(self, path, image_len=10):
        ''' build and run docker image
        '''
        os.chdir(path)
        dockerbuild = sh.Command('docker')
        random_name = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(image_len))
        image_name = '{0}'.format(random_name)
        dockerbuild('build', '-t', image_name.lower(), path)
        return image_name

    def start(self, image_name):
        #Run image
        dockerrun = sh.Command('docker')
        print(dockerrun('run', '-i', '-d', 'first/image'))

    def kill(self, id):
        ''' Kill image by id
        '''
        dockerkill = sh.Command('docker')
        dockerkill('kill', id)