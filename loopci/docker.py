import os
import sh

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


    def build(self, path):
        ''' build end run docker image
        '''
        os.chdir(path)
        dockerbuild = sh.Command('docker')
        dockerbuild('build', '-t', 'first/image', path)

    def start(self):
        #Run image
        dockerrun = sh.Command('docker')
        print(dockerrun('run', '-i', '-d', 'first/image'))

    def kill(self, id):
        ''' Kill image by id
        '''
        dockerkill = sh.Command('docker')
        dockerkill('kill', id)