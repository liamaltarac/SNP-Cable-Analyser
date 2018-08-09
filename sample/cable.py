from skrf import Network
from os.path import getctime
from time import ctime

from sample.sample import Sample
from sample.port import WirePort, Wire, CableConfiguration, EthernetPair
from parameters.type import ParameterType

class CableSample(Sample):
    @staticmethod
    def getDefaultConfiguration():
        # create the ports for this network
        ports = {
            1: WirePort(0, "12", remote=False),
            2: WirePort(1, "36", remote=False),
            3: WirePort(2, "45", remote=False),
            4: WirePort(3, "78", remote=False),
            5: WirePort(4, "12 (r)", remote=True),
            6: WirePort(5, "36 (r)", remote=True),
            7: WirePort(6, "45 (r)", remote=True),
            8: WirePort(7, "78 (r)", remote=True),
        }

        # create the wires for this network
        wires = {
            Wire("12", ports[1], ports[5], wtype=EthernetPair.PAIR12),
            Wire("36", ports[2], ports[6], wtype=EthernetPair.PAIR36),
            Wire("45", ports[3], ports[7], wtype=EthernetPair.PAIR45),
            Wire("78", ports[4], ports[8], wtype=EthernetPair.PAIR78),
        }

        # create the configuration for this network
        return CableConfiguration(foward=wires)

    @staticmethod
    def getDefaultParameters():
        return dict()

    def getAvailableParameters(self):
        return {
            ParameterType.RL,
            ParameterType.IL,
            ParameterType.NEXT,
            ParameterType.PROPAGATION_DELAY,
            ParameterType.PSNEXT,
            ParameterType.FEXT,
            ParameterType.PSFEXT,
            ParameterType.ACRF,
            ParameterType.PSACRF,
            ParameterType.LCL,
            ParameterType.LCTL,
            ParameterType.TCL,
            ParameterType.TCTL,
            ParameterType.ELTCTL,
            ParameterType.CMRL,
            ParameterType.CMNEXT,
            ParameterType.CMDMNEXT,
            ParameterType.CMDMRL,
            ParameterType.DMCMNEXT,
            ParameterType.DMCMRL, 
        }