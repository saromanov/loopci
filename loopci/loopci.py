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
        ''' run provides a main method
            for running. TODO: maybe need to change it
            to another
        '''
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
        if 'image' not in conf:
            #Build with default image
            cons = construct.RestrictConstruct("Fun construction")

        #TODO: need to leave from iteration
        value = getConfigItem(conf, 'language')
        if value is not None:
            cons.addLanguage(value)
        image = getConfigItem(conf, 'image')
        if image is not None:
            if 'version' in image:
                cons.addOS(image['name'], version=image['version'])
            else:
                const.addOS(image['name'])
        before = getConfigItem(conf, 'before_install')
        for script_key, script_value in before.items():
            cons.addScript(script_key, script_value)

        env = getConfigItem(conf, 'env')
        for env_key, env_value in env.items():
            cons.add_env_variable(env_key, env_value)
        ports = getConfigItem(conf, 'ports')
        if isinstance(ports, dict):
            for port_key, port_value in ports.items():
                cons.expose_port(port_value)
        if isinstance(ports, str):
            cons.expose_port(ports)
        cons.create_dockerfile(outpath)
        logging.info("Finished to construction Dockerfile")
        logging.info("Start to build Docker container")
        dockermanager = docker.DockerManager()
        dockermanager.build(outpath)
        logging.info("Start Docker container")
        dockermanager.start()
        #manager = docker.DockerManager()
        #docker = sh.Command("sudo docker -t build")
        #docker()


def getConfigItem(conf, name):
    ''' getConfigItem returns None if element
        is not found
    '''
    return conf[name] if name in conf else None