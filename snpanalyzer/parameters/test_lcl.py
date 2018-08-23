import unittest

from snpanalyzer.parameters.test_parameter import TestParameter
from snpanalyzer.parameters.lcl import LCL
from snpanalyzer.parameters.dataserie import PortDataSerie

class TestLCL(TestParameter):
    def createParameter(self):
        self._dataseries = {
            0: PortDataSerie(self._ports[0]),
            1: PortDataSerie(self._ports[1]),
            2: PortDataSerie(self._ports[2]),
            3: PortDataSerie(self._ports[3]),
        }

        return LCL(self._config, self._freq, self._matrices)

    def testComputeDataSeries(self):
        self.assertEqual(self._series, set(self._dataseries.values()))

    def testComputeParameter(self):
        parameter = self._parameter.getParameter()

        # there should be a parameter for each ports
        self.assertEqual(len(parameter), len(self._ports))

        # check the values of the port 0
        self.assertComplexAlmostEqual(parameter[self._dataseries[0]][0], self._matrices[0, 0, 4])
        self.assertComplexAlmostEqual(parameter[self._dataseries[0]][1], self._matrices[1, 0, 4])
        self.assertComplexAlmostEqual(parameter[self._dataseries[0]][2], self._matrices[2, 0, 4])
        self.assertComplexAlmostEqual(parameter[self._dataseries[0]][3], self._matrices[3, 0, 4])

        # check the values of the port 1
        self.assertComplexAlmostEqual(parameter[self._dataseries[1]][0], self._matrices[0, 1, 5])
        self.assertComplexAlmostEqual(parameter[self._dataseries[1]][1], self._matrices[1, 1, 5])
        self.assertComplexAlmostEqual(parameter[self._dataseries[1]][2], self._matrices[2, 1, 5])
        self.assertComplexAlmostEqual(parameter[self._dataseries[1]][3], self._matrices[3, 1, 5])

        # check the values of the port 2
        self.assertComplexAlmostEqual(parameter[self._dataseries[2]][0], self._matrices[0, 2, 6])
        self.assertComplexAlmostEqual(parameter[self._dataseries[2]][1], self._matrices[1, 2, 6])
        self.assertComplexAlmostEqual(parameter[self._dataseries[2]][2], self._matrices[2, 2, 6])
        self.assertComplexAlmostEqual(parameter[self._dataseries[2]][3], self._matrices[3, 2, 6])

        # check the values of the port 3
        self.assertComplexAlmostEqual(parameter[self._dataseries[3]][0], self._matrices[0, 3, 7])
        self.assertComplexAlmostEqual(parameter[self._dataseries[3]][1], self._matrices[1, 3, 7])
        self.assertComplexAlmostEqual(parameter[self._dataseries[3]][2], self._matrices[2, 3, 7])
        self.assertComplexAlmostEqual(parameter[self._dataseries[3]][3], self._matrices[3, 3, 7])

    def testComputeComplexParameter(self):
        parameter = self._parameter.getComplexParameter()

        # there should be a parameter for each ports
        self.assertEqual(len(parameter), len(self._ports))

        # check the values of the port 0
        self.assertEqual(parameter[self._dataseries[0]][0], self._matrices[0, 0, 4])
        self.assertEqual(parameter[self._dataseries[0]][1], self._matrices[1, 0, 4])
        self.assertEqual(parameter[self._dataseries[0]][2], self._matrices[2, 0, 4])
        self.assertEqual(parameter[self._dataseries[0]][3], self._matrices[3, 0, 4])

        # check the values of the port 1
        self.assertEqual(parameter[self._dataseries[1]][0], self._matrices[0, 1, 5])
        self.assertEqual(parameter[self._dataseries[1]][1], self._matrices[1, 1, 5])
        self.assertEqual(parameter[self._dataseries[1]][2], self._matrices[2, 1, 5])
        self.assertEqual(parameter[self._dataseries[1]][3], self._matrices[3, 1, 5])

        # check the values of the port 2
        self.assertEqual(parameter[self._dataseries[2]][0], self._matrices[0, 2, 6])
        self.assertEqual(parameter[self._dataseries[2]][1], self._matrices[1, 2, 6])
        self.assertEqual(parameter[self._dataseries[2]][2], self._matrices[2, 2, 6])
        self.assertEqual(parameter[self._dataseries[2]][3], self._matrices[3, 2, 6])

        # check the values of the port 3
        self.assertEqual(parameter[self._dataseries[3]][0], self._matrices[0, 3, 7])
        self.assertEqual(parameter[self._dataseries[3]][1], self._matrices[1, 3, 7])
        self.assertEqual(parameter[self._dataseries[3]][2], self._matrices[2, 3, 7])
        self.assertEqual(parameter[self._dataseries[3]][3], self._matrices[3, 3, 7])
if __name__ == '__main__':
    unittest.main()