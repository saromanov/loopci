import os
import sh


class DockerManager:
    ''' This class provides all about management with docker
        This class starts after construction of Dockerfile
    '''
    def __init__(self, *args, **kwargs):
        ''' TODO: Provide options for create of container
        '''
        pass

    def build(self, path):
        ''' build end run docker image
        '''
        os.chdir(path)
        dockerbuild = sh.Command('docker')
        dockerbuild('build', '-t', 'first/image', path)

    def start(self):
        #Run image
        dockerrun = sh.Command('docker')
        dockerrun('run', '-i', '-d', 'first/image')