import os

# Construct docker file

UBUNTU_INSTALL = 'apt-get install'
FEDORA_INSTALL = 'yum install'

class BaseConstruct:
    def __init__(self):
        self.result = ''

    def createDockerfile(self, path):
        f = open(path + '/Dockerfile', 'w')
        f.write(self.result)
        f.close()


class Construct(BaseConstruct):
    ''' Construct provides construction of Docker file
        It can construct from images or step by step
    '''
    def __init__(self, descr):
        BaseConstruct.__init__(self)
        self.description= descr
        self.result = ""

        #Set default os
        self.ostitle = "Ubuntu"
        self.osver = "16.04"
        self.commands = {}

    def addOS(self, title, version='latest'):
        self.result += "FROM {0} {1}\n".format(title, version)
        self.ostitle = title
        self.osver = version

    def _getInstallType(self):
        if self.ostitle in ['ubuntu', 'debain', 'mint']:
            return UBUNTU_INSTALL
        if self.ostitle in ['fedora', 'centos', 'mageia']:
            return FEDORA_INSTALL

    def addLanguage(self, title, version='0'):
        install = self._getInstallType()
        strdata = ''
        #Check if the title contans version
        #For example go:1.5 or python:3.5
        if title.find(':') != -1:
            items = title.split(':')
            title = items[0]
            version = items[1]
        if title == 'python':
            # install dependencies
            strdata += 'pip install -r requirements.txt'
            strdata += '{0} python'.format(install)
            strdata += '{0} python-dev'.format(install)

        if title == 'node':
            strdata += '{0} install npm'.format(install)
            strdata += '{0} install nodejs'.format(install)

            if version is not '0':
                strdata += 'nvm install {0}'.format(version)
                strdata += 'nvm use {0}'.format(version)

        if title == 'go':
            # install all dependencies
            strdata += 'go get ./...'
            if version is not '0':
                strdata += '{0} install golang {1}'.format(install, version)
            else :
                strdata += '{0} install golang'.format(install)

        self.result += "{0}\n".format(strdata)
        return strdata

    def addScript(self, title):
        strdata +=  'RUN {0}'.format(title)

    def addService(self, title):
        pass


    def createDockerfile(self, path):
        f = open(path + '/Dockerfile', 'w')
        f.write(self.result)
        f.close()


class RestrictConstruct(BaseConstruct):
    def __init__(self, descr):
        BaseConstruct.__init__(self)
        self.result = ''
        self.username = 'default'

    def copy_dir(self, path):
        if os.path.isdir(path) is False:
            raise Exception("{0} is not directory".format(path))
        outpath = '/usr/loopci/{0}'.format(self.username)
        dirname = os.path.dirname(path)
        splitter = dirname.split('/')
        if len(splitter) == 0:
            raise Exception("Something went wrong with getting name of directory")
        self.result += 'ADD {0} {1}\n'.format(path, outpath + '/' + splitter[-1])

    def addLanguage(self, title):
        if title.find('go') != -1:
            lang = "golang"
            version = title.split(':')[1]
            self.result += 'FROM {0}:{1}\n'.format(lang, version)

        if title.find('python') != -1:
            self.result += 'FROM {0}\n'.format(title)

        if title.find('node') != -1:
            self.result += 'FROM {0}\n'.format(title)
            self.result += 'RUN w'

    def addScript(self, key, title):
        self.result += 'RUN echo "Execution of the command {0}"\n'.format(key)
        self.result +=  'RUN {0}\n'.format(title)

    def expose_port(self, port):
        self.result += 'EXPOSE {0}\n'.format(port)

    def add_env_variable(self, key, value):
        self.result += 'RUN export {0}={1}\n'.format(key, value)

    def addInstallPackages(self, items):
        if len(items) == 0:
            return
    def add_workdir(self, dirname):
        self.result += 'ADD ./ {0}\n'.format(dirname)
        self.result += 'WORKDIR {0}\n'.format(dirname)

    def add_exec_script(self, script):
        self.result += 'CMD {0}\n'.format(script)

    def create_dockerfile(self, path):
        docker_file = open(path + '/Dockerfile', 'w')
        docker_file.write(self.result)
        docker_file.close()


