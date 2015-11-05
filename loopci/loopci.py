import sh
import construct
import asyncio
import os
import math
import logging

import docker
import construct
from config import loadConfig

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
        logging.debug("Load configuration")
        conf = loadConfig(path)
        if len(conf) == 0:
            logging.error(".loopci.hcl is empty")
            return

        #current_dir = self._createDir()
        #os.chdir(current_dir)
        logging.info("Start construction of Dockerfile")
        cons = construct.Construct("Fun construction")
        if 'image' not in conf:
            #Build with default image
            cons = construct.RestrictConstruct("Fun construction")
        for key, value in conf.items():
            if key == 'language':
                cons.addLanguage(value)
            if key == 'image':
                if 'version' in value:
                    cons.addOS(value['name'], version=value['version'])
                else:
                    const.addOS(value['name'])
        cons.createDockerfile('.')
        logging.info("Finished to construction Dockerfile")
        #manager = docker.DockerManager()
        #docker = sh.Command("sudo docker -t build")
        #docker()