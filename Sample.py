from snpAnalyze import SNPManipulations
import os
from os.path import splitext
import time

class Sample(SNPManipulations):

    '''This class handles the SNP samples for the basic test'''

    def __init__(self, snpFile, one_sided = None):


        self.snpFile = snpFile

        self.rs = super(Sample, self)
        self.rs.__init__(self.snpFile)
        #self.renumber(renumFrom, renumTo)
        self.s2mm()
        self.port_name = {0:"12", 1:"36", 2:"45", 3:"78"}

        self.name, self.extension = splitext(os.path.basename(snpFile))
        self.date = time.ctime(os.path.getctime(snpFile))
        #print self.date

        self.limit = None

        if one_sided != None:
            self.one_sided = one_sided
        
        elif self.getNumPorts(self.dd) == 4: #Assume that the test is one-sided.
                                             #This can be changed
            self.one_sided = True

        elif self.getNumPorts(self.dd) == 8: #Assume that test is end to end.
            self.one_sided = False

        self.port_name = {}
        self.pair_combo = ["45", "12","36","78"]
        
        if self.one_sided:
            for i in range(0, self.getNumPorts(self.dd)):
                self.port_name[i] = self.pair_combo[i]  #{0:"12", 1:"36", 2:"45", 3:"78"}
            self.parameters = ["RL", "NEXT", "Propagation Delay", "PSNEXT", "LCL", "TCL", "CMRL", "CMNEXT", "CMDMNEXT", "CMDMRL", "DMCMNEXT", "DMCMRL"]
        else:
            for i in range(0, self.getNumPorts(self.dd)//2):
                self.port_name[i] = self.pair_combo[i]  #{0:"12", 1:"36", 2:"45", 3:"78"}
            for i in range((self.getNumPorts(self.dd)//2), self.getNumPorts(self.dd)):
                self.port_name[i] = "(r)"+self.pair_combo[i-self.getNumPorts(self.dd)//2]  #{4:"(r)12",  :"(r)36", 6:"(r)45", 7:"(r)78", 0:"12", 1:"36", 2:"45", 3:"78"}
            self.parameters = ["RL", "IL", "NEXT", "Propagation Delay", "PSNEXT","FEXT", "PSFEXT", "ACRF", "PSACRF", "LCL", "LCTL", "TCL", "TCTL", "ELTCTL","CMRL", "CMNEXT", "CMDMNEXT", "CMDMRL", "DMCMNEXT", "DMCMRL"]

            

        #print self.port_name
        
        
        #vna_out.write_touchstone("testout_mm", form="ri")
    
        #print self.RL["RL_11"][0]

    '''@limit.setter
    def setLimit(self, ):
        self.limit = Limit()'''
        

    def getParameters(self, z=False):

        self.RL = self.getRL(self.dd, z)
        self.IL = self.getIL(self.dd, z )
        self.NEXT = self.getNEXT(self.dd, z)
        self.PropagationDelay = self.getPropagationDelay()

        self.FEXT = self.getFEXT(self.dd, z)
        self.PSNEXT = self.getPSNEXT(self.dd)
        self.PSFEXT = self.getPSFEXT(self.dd)
        self.ACRF = self.getACRF(self.dd)
        self.PSACRF = self.getPSACRF(self.dd)

        self.LCL = self.getRL(self.dc, z)
        self.LCTL = self.getIL(self.dc, z)
        self.TCL = self.getRL(self.cd, z)
        self.TCTL = self.getIL(self.cd, z)
        self.ELTCTL = self.getELTCTL()

        self.CMRL =  self.getRL(self.cc, z) #commun mode Return Loss
        self.CMNEXT =  self.getNEXT(self.cc, z) #commun mode NEXT

        self.CMDMNEXT =  self.getNEXT(self.cd, z) #commun mode NEXT
        self.CMDMRL =  self.getRL(self.cd, z) #commun mode NEXT

        self.DMCMNEXT    = self.getNEXT(self.dc, z)
        self.DMCMRL      = self.getRL(self.dc, z)
        #print self.RL.keys()

    def reCalc(self, one_sided = None):
        self.__init__(self.snpFile, one_sided)
        self.getParameters()
        

    def __retr__(self):
        return "SNP"
        
  

if __name__ == "__main__":
    
    samp = Sample('fci.s4p')
    
    samp.extractParameters(samp.dd)

    #print samp.RL["RL_11"][0]
