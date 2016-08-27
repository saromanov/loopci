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

    def run(self, path, outpath):
        logging.debug("Checking directory")
        if self._dirExist(path) is False:
            raise Exception("Directory {0} is not exist".format(path))
        if self._dirExist(outpath) is False:
            os.mkdir(outpath)

        logging.debug("Load configuration")
        conf = loadConfig(path)
        if len(conf) == 0:
            logging.error(".loopci.hcl is empty")
            return

        #current_dir = self._createDir()
        #os.chdir(current_dir)
        logging.info("Start construction of Dockerfile")
        cons = construct.Construct("Fun construction")
        print(conf)
        if 'image' not in conf:
            #Build with default image
            cons = construct.RestrictConstruct("Fun construction")

        #TODO: need to leave from iteration
        for key, value in conf.items():
            if key == 'language':
                cons.addLanguage(value)
            if key == 'image':
                if 'version' in value:
                    cons.addOS(value['name'], version=value['version'])
                else:
                    const.addOS(value['name'])
            if key == "before_install":
                for script_key, script_value in value.items():
                    cons.addScript(script_key, script_value)
            if key == "env":
                for env_key, env_value in value.items():
                    cons.add_env_variable(env_key, env_value)
            if key == 'install':
                cons.addInstallPackages(key)
        cons.createDockerfile(outpath)
        '''logging.info("Finished to construction Dockerfile")
        logging.info("Start to build Docker container")
        dockermanager = docker.DockerManager()
        dockermanager.build(outpath)
        logging.info("Start Docker container")
        dockermanager.start()'''
        #manager = docker.DockerManager()
        #docker = sh.Command("sudo docker -t build")
        #docker()