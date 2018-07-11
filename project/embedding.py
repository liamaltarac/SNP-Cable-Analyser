from project.project import Project
from project.subproject import Subproject
from project.embedding_import_dialog import EmbedImportDialog
from app.save_manager import SaveManager
from sample.single_ended import SingleEnded
from sample.deembed import Deembed
from app.component_tree_item import ComponentTreeItem
import numpy as np

class Filetype():
    OPEN = 0
    SHORT = 1
    LOAD = 2

class Embedding(Project):
    '''
    This class represents a project for analyzing plug embedding
    '''
    def __init__(self, name):
        self._sides = dict()
        self._sides["forward"] = Subproject("Forward")
        self._sides["reverse"] = Subproject("Reverse")
        super(Embedding, self).__init__(name)
        self._openSample = None
        self._shortSample = None
        self._deembedded = None
        self._plug = None

        #TODO: choose cases depending on category
        self._cases = {
            1:((0,2),(lambda f, cnext: (-38.1+20*np.log10(f/100), np.angle(cnext, deg=True)))),
            2:((0,2),(lambda f, cnext: (-38.6+20*np.log10(f/100), np.angle(cnext, deg=True)))),
            3:((0,2),(lambda f, cnext: (-39+20*np.log10(f/100), np.angle(cnext, deg=True)))),
            4:((0,2),(lambda f, cnext: (-39.5+20*np.log10(f/100), np.angle(cnext, deg=True)))),
            5:((1,2),(lambda f, cnext: (-46.5+20*np.log10(f/100), np.angle(cnext, deg=True)))),
            6:((1,2),(lambda f, cnext: (-49.5+20*np.log10(f/100), np.angle(cnext, deg=True)))),
            7:((2,3),(lambda f, cnext: (-46.5+20*np.log10(f/100), np.angle(cnext, deg=True)))),
            8:((2,3),(lambda f, cnext: (-49.5+20*np.log10(f/100), np.angle(cnext, deg=True)))),
            9:((0,1),(lambda f, cnext: (-57+20*np.log10(f/100), 90))),
            10:((0,1),(lambda f, cnext: (-70+20*np.log10(f/100), -90))),
            11:((0,3),(lambda f, cnext: (-57+20*np.log10(f/100), 90))),
            12:((0,3),(lambda f, cnext: (-70+20*np.log10(f/100), -90))),
            13:((1,3),(lambda f, cnext: (-66+20*np.log10(f/100), np.angle(cnext, deg=True)))),
            14:((1,3),(lambda f, cnext: (-66+20*np.log10(f/100), np.angle(cnext, deg=True)-180))),
            }

    def importSamples(self, fileName, fileType=Filetype.LOAD):
        if fileType == Filetype.OPEN:
            self._openSample = SingleEnded(fileName)
            self._samples.append(self._openSample)
        elif fileType == Filetype.SHORT:
            self._shortSample = SingleEnded(fileName)
            self._samples.append(self._shortSample)
        else:
            self._deembedded = Deembed(fileName, self._plug.getPlugNext(), self._plug.getNextDelay(), self._cases)
            self._samples.append(self._deembedded)

    def setPlug(self, plug):
        self._plug = plug
    
    def removeSamples(self, fileNames):
        super(Embedding, self).removeSamples(fileNames)
        if self._openSample and self._openSample.getName() in fileNames:
            self._openSample = None
        if self._shortSample and self._shortSample.getName() in fileNames:
            self._shortSample = None
        if self._deembedded and self._deembedded.getName() in fileNames:
            self._deembedded = None
        self._generateTreeStructure()

    def openImportWindow(self, parent):
        dial = EmbedImportDialog(parent)
        files = dial.getFiles()
        if files:
            load, plug, k1, k2, k3, openSample, shortSample = files
            if openSample and shortSample:
                self.importSamples(openSample, Filetype.OPEN)
                self.importSamples(shortSample, Filetype.SHORT)
            plugProject = SaveManager().loadProject(plug)
            self.setPlug(plugProject)
            self.importSamples(load, Filetype.LOAD)
            self._sides["forward"].setComponents(self._samples)
            self._sides["forward"].addComponent(plugProject)
            self._generateTreeStructure()

    def generateExcel(self, outputName, sampleNames, z=False):
        raise NotImplementedError

    def _generateTreeStructure(self):
        self._treeItem.children = list()
        for side in self._sides.values():
            self._treeItem.addChild(side.getTreeItem())