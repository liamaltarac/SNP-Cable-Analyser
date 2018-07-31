from sample.sample import Sample, PORTS_NAME
from sample.port import EthernetPair, NetworkPort, PlugConfiguration
from parameters.type import ParameterType

class PlugSample(Sample):
    def getDefaultConfiguration(self):
        # create the ports for this network
        ports = {
            NetworkPort(0, "12", ptype=EthernetPair.PAIR12),
            NetworkPort(1, "36", ptype=EthernetPair.PAIR36),
            NetworkPort(2, "45", ptype=EthernetPair.PAIR45),
            NetworkPort(3, "78", ptype=EthernetPair.PAIR78),
        }

        # create the configuration for this network
        return PlugConfiguration(ports=ports)

    def getDefaultParameters(self):
        return dict()

    def getAvailableParameters(self):
        return {
            ParameterType.RL,
            ParameterType.NEXT,
            ParameterType.PROPAGATION_DELAY,
            ParameterType.PSNEXT,
            ParameterType.LCL,
            ParameterType.TCL,
            ParameterType.CMRL,
            ParameterType.CMNEXT,
            ParameterType.CMDMNEXT,
            ParameterType.CMDMRL,
            ParameterType.DMCMNEXT,
            ParameterType.DMCMRL, 
        }
        
