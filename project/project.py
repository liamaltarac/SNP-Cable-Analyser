from sample.end_to_end import EndToEnd
from sample.single_ended import SingleEnded
from multiprocessing.dummy import Pool as ThreadPool
from os.path import splitext
import xlsxwriter
from app.component_tree_item import ComponentTreeItem
from app.component import Component
from PyQt5 import QtWidgets

class Project(Component):
    '''
    The project class represents a simple project containing a number of regular samples.
    '''

    def __init__(self, name):
        super(Project, self).__init__(name)
        self._samples = list()
        self.recreateTreeStructure()

    def importSamples(self, fileNames):
        pool = ThreadPool()
        self._samples.extend(pool.map(self.__createSample, fileNames))

    def removeSamples(self, names):
        self._samples = [x for x in self._samples if x.getName() not in names]
        self._generateTreeStructure()

    def generateExcel(self, outputName, sampleNames, z=False):
        workbook = xlsxwriter.Workbook(outputName, options={'nan_inf_to_errors': True})
        samples = [x for x in self._samples if x.getName() in sampleNames]
        for i,sample in enumerate(samples):
            try:
                worksheet = workbook.add_worksheet(sample.getName())
            except:
                worksheet = workbook.add_worksheet(sample.getName()+str(i))
            worksheet.write('A1', 'Sample ID:')
            worksheet.write('B1', sample.getName())

            cell_format = workbook.add_format({'align': 'center',
                                                'valign': 'vcenter',
                                                'border': 6,})
            worksheet.merge_range('A3:A5', "Frequency", cell_format)

            curPos = 1
            for i, (paramName, parameter) in enumerate(sample.getParameters().items()):
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
                        if z:
                            worksheet.write(4,curPos+i*2, "real", cell_format)
                            worksheet.write(4,curPos+i*2+1, "imaginary", cell_format)
                            param = parameter.getComplexParameter()
                            for j,data in enumerate(param[key]):
                                worksheet.write(5+j, 0, sample.getFrequencies()[j])
                                self.box(workbook, worksheet, param, key, i*2, j, data.real, curPos)
                                self.box(workbook, worksheet, param, key, i*2+1, j, data.imag, curPos)
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

    def box(self, workbook, worksheet, parameter, port, i, j, data, curPos):
        box_form = workbook.add_format()
        if j == 0:
            box_form.set_top(6)
        if i == 0:
            box_form.set_left(6)
        if j == len(parameter[port])-1:
            box_form.set_bottom(6)
        if i == len(parameter)*2-1:
            box_form.set_right(6)
        worksheet.write(j+5, curPos+i, data, box_form)

    def findSamplesByName(self, names):
        return [x for x in self._samples if x.getName() in names]

    def numSamples(self):
        return len(self._samples)

    def samples(self):
        return self._samples

    def openImportWindow(self, parent):
        names,_ = QtWidgets.QFileDialog.getOpenFileNames(parent, caption="Select SNP(s)", directory="",filter="sNp Files (*.s*p)")
        if names:
            self.importSamples(names)
            self._generateTreeStructure()

    def recreateTreeStructure(self):
        self._treeItem = ComponentTreeItem(self)
        self._generateTreeStructure()

    def __createSample(self, name):
        _, extension = splitext(name)
        if extension[2] == "8" or extension[2] == "4":
            return SingleEnded(name)
        return EndToEnd(name)
        
    def _generateTreeStructure(self):
        self._treeItem.children = list()
        for sample in self._samples:
            self._treeItem.addChild(sample.getTreeItem())
