import sh
import construct
import asyncio
import os
import math
import logging

import docker

logging.basicConfig(level=logging.DEBUG)

class Loopci:
    def __init__(self, *args, **kwargs):
        pass

    def _createDir(self):
        return "dir"

    def _dirExist(self, path):
        return os.path.isdir(path)

    def run(self, path):
        logging.debug("Checking directory")
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