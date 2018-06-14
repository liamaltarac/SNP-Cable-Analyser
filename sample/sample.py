from sample.snp_analyzer import SNPAnalyzer

PORTS_NAME = ["12", "45", "36", "78"]
class Sample(object):
    '''
    The sample class contains the measurements for one object
    '''
    def __init__(self, snpFile):
        self._parameters = dict()
        if snpFile:
            self._snp = SNPAnalyzer(snpFile)
            self._mm, self._freq, self._portsNumber = self._snp.getMM()
            self._name, self._extension, self._date = self._snp.getFileInfo()
            self._ports = dict()
            self.setPorts()
            self.addParameters()


    def addParameters(self):
        raise NotImplementedError

    def setStandard(self, standard):
        for name, parameter in self._parameters:
            parameter.setLimit(standard.limits[name])

    def parameters(self):
        return self._parameters

    def setPorts(self):
        for i in range(self._portsNumber):
            self._ports[i] = PORTS_NAME[i]
    