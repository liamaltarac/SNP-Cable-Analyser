from snpanalyzer.parameters.returnloss import ReturnLoss
from snpanalyzer.parameters.parameter import diffComMatrix
from snpanalyzer.parameters.type import ParameterType

class LCL(ReturnLoss):
    '''
    LCL is calculated using the return loss in Differential-Common (DC) mode.
    
    Example of LCL with 4 wires
        
             1 2 3 4
        1  [ 1 _ _ _ ] 
        2  [ _ 2 _ _ ] 
        3  [ _ _ 3 _ ] 
        4  [ _ _ _ 4 ] 
    '''
    @staticmethod
    def getType():
        return ParameterType.LCL

    @staticmethod
    def register(parameters):
        return lambda c, f, m: LCL(c, f, m)

    def chooseMatrices(self, matrices):
        return diffComMatrix(matrices)

    def getName(self):
        return "LCL"
