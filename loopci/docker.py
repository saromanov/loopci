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

    def start(path):
        ''' build end run docker image
        '''
        os.chdir(path)
        dockerbuild = sh.Command('docker build -n first/image .')
        dockerbuild()
        #Run image
        dockerrun = sh.Command('docker run -i -t first/image')
        dockerrun()