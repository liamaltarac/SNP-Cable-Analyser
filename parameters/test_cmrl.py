import unittest

from parameters.parameter import complex2db
from parameters.test_parameter import TestParameter
from parameters.cmrl import CMRL

class TestCMRL(TestParameter):
    def testComputeParameter(self):
        pCMRL = CMRL(self._ports, self._freq, self._matrices)
        parameter = pCMRL.getParameter()

        # there should be a parameter for each ports
        self.assertEqual(len(parameter), len(self._ports))

        # the number of sample should be the same as the number of frequencies
        self.assertEqual(len(parameter[0]), len(self._freq))
        self.assertEqual(len(parameter[1]), len(self._freq))
        self.assertEqual(len(parameter[2]), len(self._freq))
        self.assertEqual(len(parameter[3]), len(self._freq))

        # check the values of the port 1
        self.assertEqual(parameter[0][0], complex2db(self._matrices[0, 4, 4]))
        self.assertEqual(parameter[0][1], complex2db(self._matrices[1, 4, 4]))
        self.assertEqual(parameter[0][2], complex2db(self._matrices[2, 4, 4]))
        self.assertEqual(parameter[0][3], complex2db(self._matrices[3, 4, 4]))

        # check the values of the port 2
        self.assertEqual(parameter[1][0], complex2db(self._matrices[0, 5, 5]))
        self.assertEqual(parameter[1][1], complex2db(self._matrices[1, 5, 5]))
        self.assertEqual(parameter[1][2], complex2db(self._matrices[2, 5, 5]))
        self.assertEqual(parameter[1][3], complex2db(self._matrices[3, 5, 5]))

        # check the values of the port 3
        self.assertEqual(parameter[2][0], complex2db(self._matrices[0, 6, 6]))
        self.assertEqual(parameter[2][1], complex2db(self._matrices[1, 6, 6]))
        self.assertEqual(parameter[2][2], complex2db(self._matrices[2, 6, 6]))
        self.assertEqual(parameter[2][3], complex2db(self._matrices[3, 6, 6]))

        # check the values of the port 4
        self.assertEqual(parameter[3][0], complex2db(self._matrices[0, 7, 7]))
        self.assertEqual(parameter[3][1], complex2db(self._matrices[1, 7, 7]))
        self.assertEqual(parameter[3][2], complex2db(self._matrices[2, 7, 7]))
        self.assertEqual(parameter[3][3], complex2db(self._matrices[3, 7, 7]))

    def testComputeComplexParameter(self):
        pCMRL = CMRL(self._ports, self._freq, self._matrices)
        parameter = pCMRL.getComplexParameter()

        # there should be a parameter for each ports
        self.assertEqual(len(parameter), len(self._ports))

        # the number of sample should be the same as the number of frequencies
        self.assertEqual(len(parameter[0]), len(self._freq))
        self.assertEqual(len(parameter[1]), len(self._freq))
        self.assertEqual(len(parameter[2]), len(self._freq))
        self.assertEqual(len(parameter[3]), len(self._freq))

        # check the values of the port 1
        self.assertEqual(parameter[0][0], self._matrices[0, 4, 4])
        self.assertEqual(parameter[0][1], self._matrices[1, 4, 4])
        self.assertEqual(parameter[0][2], self._matrices[2, 4, 4])
        self.assertEqual(parameter[0][3], self._matrices[3, 4, 4])

        # check the values of the port 2
        self.assertEqual(parameter[1][0], self._matrices[0, 5, 5])
        self.assertEqual(parameter[1][1], self._matrices[1, 5, 5])
        self.assertEqual(parameter[1][2], self._matrices[2, 5, 5])
        self.assertEqual(parameter[1][3], self._matrices[3, 5, 5])

        # check the values of the port 3
        self.assertEqual(parameter[2][0], self._matrices[0, 6, 6])
        self.assertEqual(parameter[2][1], self._matrices[1, 6, 6])
        self.assertEqual(parameter[2][2], self._matrices[2, 6, 6])
        self.assertEqual(parameter[2][3], self._matrices[3, 6, 6])

        # check the values of the port 4
        self.assertEqual(parameter[3][0], self._matrices[0, 7, 7])
        self.assertEqual(parameter[3][1], self._matrices[1, 7, 7])
        self.assertEqual(parameter[3][2], self._matrices[2, 7, 7])
        self.assertEqual(parameter[3][3], self._matrices[3, 7, 7])

if __name__ == '__main__':
    unittest.main()
