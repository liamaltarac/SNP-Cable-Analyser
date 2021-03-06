from snpanalyzer.sample.plug import PlugSample
from snpanalyzer.parameters.type import ParameterType

class DeembedSample(PlugSample):
    def __init__(self, snp, plugNext, plugNEXTDelay, cases, **kwargs):
        self._plugNEXT = plugNext
        self._plugNEXTDelay = plugNEXTDelay
        self._cases = cases
        super(DeembedSample, self).__init__(snp, **kwargs)

    def getDefaultParameters(self):
        return dict([
            (ParameterType.PC_NEXT   , self._plugNEXT),
            (ParameterType.NEXT_DELAY, self._plugNEXTDelay),
            (ParameterType.CASES     , self._cases)])


    def getAvailableParameters(self):
        return [
            ParameterType.RL,
            ParameterType.NEXT,
            ParameterType.DNEXT,
            ParameterType.CASE,
        ]

    def getAvailableExport(self):
        return [
            ParameterType.RL,
            ParameterType.NEXT,
            ParameterType.DNEXT,
        ]

    def setStandard(self, standard):
        super(DeembedSample, self).setStandard(standard)
        for name, parameter in self._parameters.items():
            if name.name == "CASE":
                parameter.setLimit(standard.limits["NEXT"])

class ReverseDeembedSample(DeembedSample):
    def __init__(self, snp, plugNext, plugDelay, jackOpenDelay, jackShortDelay, k1, k2, k3, cases, **kwargs):
        self._plugNEXT = plugNext
        self._jackOpenDelay = jackOpenDelay
        self._jackShortDelay = jackShortDelay
        self._plugDelay = plugDelay
        self._cases = cases
        self._k1 = k1
        self._k2 = k2
        self._k3 = k3
        PlugSample.__init__(self, snp, **kwargs)

    def getDefaultParameters(self):
        return {
            ParameterType.PC_NEXT           : self._plugNEXT,
            ParameterType.PLUG_DELAY        : self._plugDelay,
            ParameterType.JACK_OPEN_DELAY   : self._jackOpenDelay,
            ParameterType.JACK_SHORT_DELAY  : self._jackShortDelay,
            ParameterType.CASES             : self._cases,
            ParameterType.K1                : self._k1,
            ParameterType.K2                : self._k2,
            ParameterType.K3                : self._k3,
        }

    def getAvailableParameters(self):
        return [
            ParameterType.RL,
            ParameterType.NEXT,
            ParameterType.RDNEXT,
            ParameterType.RCASE,
        ]
    def getAvailableExport(self):
        return[
            ParameterType.RL,
            ParameterType.NEXT,
            ParameterType.RDNEXT,
        ]

    def setStandard(self, standard):
        super(ReverseDeembedSample, self).setStandard(standard)
        for name, parameter in self._parameters.items():
            if name.name == "RCASE":
                parameter.setLimit(standard.limits["NEXT"])
