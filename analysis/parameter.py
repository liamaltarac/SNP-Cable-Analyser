from matplotlib import pyplot as plt
from analysis.figure import FigureAnalysis
from analysis.format import DataFormat, formatParameterData
from analysis.scale import PlotScale
from document.parameter import ParameterDocumentObject
from overrides import overrides

class ParameterAnalysis(FigureAnalysis):
    def __init__(self, parameter, **kwargs):
        self._parameter = parameter
        self._series = set()
        super(ParameterAnalysis, self).__init__(**kwargs)

        # by default, we show all series
        for serie in self._parameter.getDataSeries():
            self.addSerie(serie)

    @overrides
    def _getXData(self, serie):
        return self._parameter.getFrequencies()

    @overrides
    def _getYData(self, serie):
        return formatParameterData(self._parameter, serie, self.getFormat())

    @overrides
    def _getLabel(self, serie):
        return serie.getName()

    @overrides
    def getDefaultTitle(self):
        return self._parameter.getName()

    @overrides
    def getDefaultScale(self):
        return PlotScale.LOGARITHMIC

    @overrides
    def getDefaultFormat(self):
        # we prefer magnitude when available
        formats = self._parameter.getAvailableFormats()
        if DataFormat.MAGNITUDE in formats:
            return DataFormat.MAGNITUDE

        # else choose any format
        return next(iter(formats))

    @overrides
    def getMaximumNumberOfLines(self):
        return len(self._parameter.getDataSeries())

    @overrides
    def getAvailableFormats(self):
        return self._parameter.getAvailableFormats()

    def addSerie(self, serie):
        # make sure the serie isn't already in the figure
        if serie in self._series:
            return

        # add the serie
        self._addLine(serie)
        self._series.add(serie)

    def removeSerie(self, serie):
        # make sure the serie is in the figure
        if serie not in self._series:
            return

        # remove the serie
        self._removeLine(serie)
        self._series.discard(serie)

    def getParameter(self):
        return self._parameter

    @overrides
    def generateDocumentObject(self, prefix):
        return ParameterDocumentObject(prefix, self)
        