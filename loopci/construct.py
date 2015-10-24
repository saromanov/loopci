
# Construct docker file

UBUNTU_INSTALL = 'apt-get install'
FEDORA_INSTALL = 'yum install'


class Construct:
    ''' Construct provides construction of Docker file
    '''
    def __init__(self, descr):
        self.description= descr
        self.result = ""

        #Set default os
        self.ostitle = "Ubuntu"
        self.osver = "14.04"

    def addOS(self, title, version):
        self.result += "FROM {0} {1}\n".format(title, version)
        self.ostitle = title
        self.osver = version

    def _getInstallType(self):
        if self.ostitle in ['ubuntu', 'debain', 'mint']:
            return UBUNTU_INSTALL
        if self.ostitle in ['fedora', 'centos', 'mageia']:
            return FEDORA_INSTALL

    def addLanguage(self, title, version):
        install = self._getInstallType()
        strdata = ''
        if title == 'python':
            strdata += '{0} python'.format(install)
            strdata += '{0} python-dev'.format(install)

        if title == 'node':
            strdata += '{0} install npm'.format(install)
            strdata += '{0} install nodejs'.format(install)
            strdata += 'nvm install {0}'.format(version)
            strdata += 'nvm use {0}'.format(version)

        if title == 'go':
            strdata += '{0} install golang'.format(install)

        self.result += "{0}\n".format(strdata)
        return strdata

    def addService(self, title):
        pass


    def createDockerfile(self, path):
        f = open(path + '/Dockerfile', 'w')
        f.write(self.result)
        f.close()