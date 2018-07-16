from sample.sample import Sample, PORTS_NAME
from parameters.parameter_factory import ParameterFactory

class Disturber(Sample):
    '''
    The Disturber class contains the measurements for alien parameters of one disturber on the victim
    '''
    def __init__(self, snpFile, param="ANEXT"):
        self._param = param
        super(Disturber, self).__init__(snpFile)
    
    def addParameters(self):
        parameters = [
            "IL",
            "FEXT",
            self._param,
        ]

        for parameter in parameters:
            self._parameters[parameter] = self._factory.getParameter(parameter)

    def setPorts(self):
        for i in range(self._portsNumber//2):
            self._ports[i] = (PORTS_NAME[i], False)
            self._ports[i+self._portsNumber//2] = ("(d)"+PORTS_NAME[i], True)