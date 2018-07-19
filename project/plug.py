from project.project import Project, ProjectNode
from sample.delay import Delay
from sample.plug_sample import PlugSample
from project.plug_import_dialog import PlugImportDialog
import numpy as np
import xlsxwriter

class Plug(Project):

    def __init__(self, name):
        super(Plug, self).__init__(name)
        self._openDelay = None
        self._shortDelay = None
        self._loadSample = None
        self._dfOpenDelay = None
        self._dfShortDelay = None
        self._k1 = 0
        self._k2 = 0
        self._k3 = 0

    def importDfOpen(self, fileName):
        self._dfOpenDelay = Delay(fileName)
        return self._dfOpenDelay

    def importDfShort(self, fileName):
        self._dfShortDelay = Delay(fileName)
        return self._dfShortDelay

    def importOpen(self, fileName):
        self._openDelay = Delay(fileName)
        return self._openDelay

    def importShort(self, fileName):
        self._shortDelay = Delay(fileName)
        return self._shortDelay

    def importLoad(self, fileName):
        self._loadSample = PlugSample(fileName, 
            self._openDelay.getParameters()["Propagation Delay"],
            self._shortDelay.getParameters()["Propagation Delay"],
            self._dfOpenDelay.getParameters()["Propagation Delay"],
            self._dfShortDelay.getParameters()["Propagation Delay"],
            self._k1, self._k2, self._k3)
        return self._loadSample

    def getPlugNext(self):
        return self._loadSample.getParameters()["CNEXT"]

    def getNextDelay(self):
        return self._loadSample.getParameters()["NEXTDelay"]

    def setConstants(self, k1, k2, k3):
        self._k1 = k1
        self._k2 = k2
        self._k3 = k3

    def recalculate(self):
        self._loadSample.recalculate(self._k1, self._k2, self._k3)

    def getConstants(self):
        return (self._k1, self._k2, self._k3)

    def nodeFromProject(self):
        return PlugNode(self)

    def removeSample(self, sample):
        if self._dfOpenDelay == sample:
            self._dfOpenDelay = None
        if self._dfShortDelay == sample:
            self._dfShortDelay = None
        if self._openDelay == sample:
            self._openDelay = None
        if self._shortDelay == sample:
            self._shortDelay = None
        if self._loadSample == sample:
            self._loadSample = None

    def generateExcel(self, outputName, sampleNames, z=False):
        workbook = xlsxwriter.Workbook(outputName, options={'nan_inf_to_errors': True})
        sample = self._loadSample
        worksheet = workbook.add_worksheet(sample.getName())
        worksheet.write('A1', 'Plug ID:')
        worksheet.write('B1', sample.getName())
    
        cell_format = workbook.add_format({'align': 'center',
                                            'valign': 'vcenter',
                                            'border': 6,})
        worksheet.merge_range('A3:A5', "Frequency", cell_format)

        curPos = 1
        parameters = {"RL": sample.getParameters()["RL"], "CNEXT": sample.getParameters()["CNEXT"]}
        for i, (paramName, parameter) in enumerate(parameters.items()):
            numSignals = len(parameter.getPorts())
            worksheet.merge_range(2, curPos, 2, curPos+numSignals*2-1,  paramName, cell_format)
            for i, (key, (portName,_)) in enumerate(parameter.getPorts().items()):
                worksheet.merge_range(3, curPos+i*2, 3, curPos+i*2+1, str(portName), cell_format)
                if paramName == "Propagation Delay":
                    worksheet.merge_range(4, curPos+i*2, 4, curPos+i*2+1, "ns", cell_format)
                    param = parameter.getParameter()
                    for j, data in enumerate(param[key]):
                        worksheet.merge_range(5+j, curPos+i*2, 5+j, curPos+i*2+1, "")
                        self.box(workbook, worksheet, param, key, i*2, j, data, curPos)
                else:
                    worksheet.write(4,curPos+i*2, "mag", cell_format)
                    worksheet.write(4,curPos+i*2+1, "phase", cell_format)
                    param = parameter.getParameter()
                    for j, (mag, phase) in enumerate(param[key]):
                        worksheet.write(5+j, 0, sample.getFrequencies()[j])
                        self.box(workbook, worksheet, param, key, i*2, j, mag, curPos)
                        self.box(workbook, worksheet, param, key, i*2+1, j, phase, curPos)
        
            curPos += numSignals*2
        workbook.close()

from sample.sample import SampleNode
from widgets.plug_widget import PlugWidget

class PlugNode(ProjectNode):
    def __init__(self, plug):
        super(PlugNode, self).__init__(plug)
        self._plugWidget = None

    def openImportWindow(self, parent):
        dial = PlugImportDialog(parent)
        files = dial.getFiles()
        if files:
            dfOpen, dfShort, plugOpen, plugShort, plugLoad, k1, k2, k3 = files
            openSample = self._dataObject.importOpen(plugOpen)
            shortSample = self._dataObject.importShort(plugShort)
            dfOpenSample = self._dataObject.importDfOpen(dfOpen)
            dfShortSample = self._dataObject.importDfShort(dfShort)
            self._dataObject.setConstants(k1, k2, k3)
            loadSample = self._dataObject.importLoad(plugLoad)

            samples = [openSample, shortSample, dfOpenSample, dfShortSample, loadSample]
            self.addChildren(samples)
            if self._plugWidget:
                self._plugWidget.createTabs()
                self._plugWidget.updateWidget()

    def addChildren(self, samples):
        for sample in samples:
            self.appendRow(SampleNode(sample, self._dataObject))

    def setupInitialData(self):
        samples = list()
        if self._dataObject._openDelay:
            samples.append(self._dataObject._openDelay)
        if self._dataObject._shortDelay:
            samples.append(self._dataObject._shortDelay)
        if self._dataObject._dfOpenDelay:
            samples.append(self._dataObject._dfOpenDelay)
        if self._dataObject._dfShortDelay:
            samples.append(self._dataObject._dfShortDelay)
        if self._dataObject._loadSample:
            samples.append(self._dataObject._loadSample)
        self.addChildren(samples)

    def getWidgets(self):
        if not self._plugWidget:
            self._plugWidget = PlugWidget(self)
        return {"Plug": self._plugWidget}