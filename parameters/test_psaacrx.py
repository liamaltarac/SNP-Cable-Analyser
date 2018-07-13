import unittest
from parameters.test_parameter import TestParameter
from parameters.insertionloss import InsertionLoss
from parameters.psaxext import PSAXEXT
from parameters.psaacrx import PSAACRX
from parameters.axext import AXEXT
from parameters.fext import FEXT
from parameters.dataserie import PortDataSerie, PortPairDataSerie

class TestPSAACRX(TestParameter):
    def createParameter(self):
        # we assume that psfext and il are tested
        self._il   = InsertionLoss(self._config, self._freq, self._matrices, reverse=False)
        self._fext = FEXT(self._config, self._freq, self._matrices, reverse=False)
        self._axextd  = {
            0: AXEXT(self._config, self._freq, self._matrices, self._fext, self._il),
            1: AXEXT(self._config, self._freq, self._matrices, self._fext, self._il),
            2: AXEXT(self._config, self._freq, self._matrices, self._fext, self._il),
            3: AXEXT(self._config, self._freq, self._matrices, self._fext, self._il),
        }

        self._dataseries = {
            0: PortDataSerie(self._ports[0]),
            1: PortDataSerie(self._ports[1]),
        }

        self._pairseries = {
            0: PortPairDataSerie(self._ports[0], self._ports[2]),
            1: PortPairDataSerie(self._ports[1], self._ports[3]),
        }

        self._expected = {
            self._dataseries[0]: self._pairseries[0],
            self._dataseries[1]: self._pairseries[1],
        }

        self._psaxext = PSAXEXT(self._config, self._freq, self._matrices, self._axextd.values())

        return PSAACRX(self._config, self._freq, self._matrices, self._psaxext, self._il)

    def testComputeDataSeries(self):
        for expected in self._expected:
            self.assertIn(expected, self._series)

    def testComputeParameter(self):
        parameter = self._parameter.getParameter()
        
        dbPSAXEXT = self._parameter.getPSAXEXT().getParameter()
        dbIL      = self._parameter.getIL().getParameter()

        for serie in self._dataseries.values():
            # the number of sample should be the same as the number of frequencies
            self.assertEqual(len(parameter[serie]), len(self._freq))

            # check the values of this port
            pair = self._expected[serie]
            self.assertAlmostEqual(parameter[serie][0][0], dbPSAXEXT[serie][0][0]-dbIL[pair][0][0])
            self.assertAlmostEqual(parameter[serie][1][0], dbPSAXEXT[serie][1][0]-dbIL[pair][1][0])
            self.assertAlmostEqual(parameter[serie][2][0], dbPSAXEXT[serie][2][0]-dbIL[pair][2][0])
            self.assertAlmostEqual(parameter[serie][3][0], dbPSAXEXT[serie][3][0]-dbIL[pair][3][0])

if __name__ == '__main__':
    unittest.main()
