import sh
import construct
import asyncio
import os
import math

import docker

class Loopci:
    def __init__(self):
        pass

    def _createDir(self):
        return "dir"

    def run(self):
        current_dir = self._createDir()
        os.chdir(current_dir)
        cons = Construct("Fun construction")
        dock = Docker()
        dock.start('.')
        docker = sh.Command("sudo docker -t build")
        docker()