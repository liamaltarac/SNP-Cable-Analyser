import unittest
from parameters.parameter import complex2phase
from parameters.test_parameter import TestParameter
from parameters.propagationdelay import PropagationDelay
from parameters.returnloss import ReturnLoss
from parameters.dfdelay import DFDelay
from parameters.plugdelay import PlugDelay
import numpy as np

class TestPlugDelay(TestParameter):
    def setUp(self):
        self._ports = {
            0: ("Port 1", False),
            1: ("Port 2", False),
            2: ("Port 3", False),
            3: ("Port 4", False),
        }
        self._matrices = np.array([
            [
                [complex(x,2*(z%2-1/2)*x) for x in range(8*y+1,8*(y+1)+1)] for y in range(8*z, 8*(z+1))
            ] for z in range(4)
        ], np.complex)
        self._freq = [100, 200, 300, 500]
        self._parameter = self.createParameter()
 
    def createParameter(self):
        rl = ReturnLoss(self._ports, self._freq, self._matrices)
        opendfDelay = PropagationDelay(self._ports, self._freq, self._matrices, rl)
        shortdfDelay = PropagationDelay(self._ports, self._freq, self._matrices, rl)
        dfDelay = DFDelay(self._ports, self._freq, self._matrices, opendfDelay, shortdfDelay)
        openDelay = PropagationDelay(self._ports, self._freq, self._matrices, rl)
        shortDelay = PropagationDelay(self._ports, self._freq, self._matrices, rl)

        k1 = 1
        k2 = 2
        k3 = 3
        return PlugDelay(self._ports, self._freq, self._matrices, openDelay, shortDelay, dfDelay, k1, k2, k3)

    def testComputeParameter(self):
        parameter = self._parameter.getParameter()
        openDelay = self._parameter.getOpenDelay().getParameter()
        shortDelay = self._parameter.getShortDelay().getParameter()
        dfDelay = self._parameter.getDFDelay().getParameter()

        # there should be a parameter for each ports
        self.assertEqual(len(parameter), len(self._ports))
        
        # check the values of the port 1
        self.assertAlmostEqual(parameter[(0,0)], (np.mean(openDelay[(0,0)]) + np.mean(shortDelay[(0,0)]) - 3)/4.0 - dfDelay[(0,0)] + 3)
        # check the values of the port 2
        self.assertAlmostEqual(parameter[(1,1)], (np.mean(openDelay[(1,1)]) + np.mean(shortDelay[(1,1)]) - 3)/4.0 - dfDelay[(1,1)] + 3)
        # check the values of the port 3
        self.assertAlmostEqual(parameter[(2,2)], (np.mean(openDelay[(2,2)]) + np.mean(shortDelay[(2,2)]) - 3)/4.0 - dfDelay[(2,2)] + 3)
        # check the values of the port 4
        self.assertAlmostEqual(parameter[(3,3)], (np.mean(openDelay[(3,3)]) + np.mean(shortDelay[(3,3)]) - 3)/4.0 - dfDelay[(3,3)] + 3)

if __name__ == '__main__':
    unittest.main()
