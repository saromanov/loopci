import sh
import construct
import asyncio
import os
import math

import docker

class Loopci:
    def __init__(self, *args, **kwargs):
        pass

    def _createDir(self):
        return "dir"

    def _dirExist(self, path):
        return os.path.isdir(path)

    def run(self, path):
        if self._dirExist(path) is False:
            raise Exception("Directory {0} is not exist".format(path))
        current_dir = self._createDir()
        os.chdir(current_dir)
        cons = Construct("Fun construction")
        dock = Docker()
        dock.start('.')
        manager = docker.DockerManager()
        #docker = sh.Command("sudo docker -t build")
        #docker()