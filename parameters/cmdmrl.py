from parameters.returnloss import ReturnLoss
from parameters.parameter import comDiffMatrix
from parameters.type import ParameterType

class CMDMRL(ReturnLoss):
    '''
    CMDMRL is calculated using the Return Loss of the common mode - differential mode (cd) matrix

    Example of CMDMRL with 4 wires
        
             1 2 3 4
        1  [ 1 _ _ _ ] 
        2  [ _ 2 _ _ ] 
        3  [ _ _ 3 _ ] 
        4  [ _ _ _ 4 ] 
    '''
    @staticmethod
    def getType():
        return ParameterType.CMDMRL

    def chooseMatrices(self, matrices):
        return comDiffMatrix(matrices)

    def getName(self):
        return "CMDMRL"
