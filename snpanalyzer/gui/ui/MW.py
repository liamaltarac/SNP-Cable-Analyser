# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QAction


class Ui_MainWindow(object):
    actionCalibrate: QAction

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(896, 683)
        MainWindow.setMinimumSize(QtCore.QSize(896, 683))
        MainWindow.setWindowOpacity(42.0)
        MainWindow.setUnifiedTitleAndToolBarOnMac(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.splitter_2 = QtWidgets.QSplitter(self.centralwidget)
        self.splitter_2.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.splitter_2.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_2.setOpaqueResize(True)
        self.splitter_2.setHandleWidth(10)
        self.splitter_2.setChildrenCollapsible(False)
        self.splitter_2.setObjectName("splitter_2")
        self.sampleTable = QtWidgets.QTreeView(self.splitter_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sampleTable.sizePolicy().hasHeightForWidth())
        self.sampleTable.setSizePolicy(sizePolicy)
        self.sampleTable.setMinimumSize(QtCore.QSize(50, 507))
        self.sampleTable.setMaximumSize(QtCore.QSize(300, 16777215))
        self.sampleTable.setAlternatingRowColors(True)
        self.sampleTable.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.sampleTable.setObjectName("sampleTable")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.splitter_2)
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.splitter = QtWidgets.QSplitter(self.verticalLayoutWidget)
        self.splitter.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setOpaqueResize(True)
        self.splitter.setHandleWidth(10)
        self.splitter.setChildrenCollapsible(False)
        self.splitter.setObjectName("splitter")
        self.param_tabs = QtWidgets.QTabWidget(self.splitter)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(100)
        sizePolicy.setHeightForWidth(self.param_tabs.sizePolicy().hasHeightForWidth())
        self.param_tabs.setSizePolicy(sizePolicy)
        self.param_tabs.setObjectName("param_tabs")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.param_tabs.addTab(self.tab, "")
        self.verticalLayout_3.addWidget(self.splitter)
        self.verticalLayout_4.addWidget(self.splitter_2)
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setMinimum(0)
        self.progressBar.setMaximum(100)
        self.progressBar.setTextVisible(True)
        self.progressBar.setObjectName("progressBar")
        self.verticalLayout_4.addWidget(self.progressBar)
        self.horizontalLayout_3.addLayout(self.verticalLayout_4)
        MainWindow.setCentralWidget(self.centralwidget)
        self.toolBar2 = QtWidgets.QToolBar(MainWindow)
        self.toolBar2.setMovable(False)
        self.toolBar2.setObjectName("toolBar2")
        MainWindow.addToolBar(QtCore.Qt.RightToolBarArea, self.toolBar2)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setEnabled(True)
        font = QtGui.QFont()
        font.setStrikeOut(False)
        self.toolBar.setFont(font)
        self.toolBar.setMovable(False)
        self.toolBar.setFloatable(True)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 896, 21))
        self.menuBar.setObjectName("menuBar")
        self.menuFile = QtWidgets.QMenu(self.menuBar)
        self.menuFile.setObjectName("menuFile")
        self.menuEdit = QtWidgets.QMenu(self.menuBar)
        self.menuEdit.setObjectName("menuEdit")
        self.menuSettings = QtWidgets.QMenu(self.menuBar)
        self.menuSettings.setObjectName("menuSettings")
        self.menuVNA = QtWidgets.QMenu(self.menuBar)
        self.menuVNA.setObjectName("menuVNA")
        MainWindow.setMenuBar(self.menuBar)
        self.actionImport_SnP = QtWidgets.QAction(MainWindow)
        self.actionImport_SnP.setObjectName("actionImport_SnP")
        self.actionImport_Project = QtWidgets.QAction(MainWindow)
        self.actionImport_Project.setCheckable(False)
        self.actionImport_Project.setChecked(False)
        self.actionImport_Project.setObjectName("actionImport_Project")
        self.actionSave_Project = QtWidgets.QAction(MainWindow)
        self.actionSave_Project.setObjectName("actionSave_Project")
        self.actionSave_Project.setEnabled(False)
        self.actionExport_Excel = QtWidgets.QAction(MainWindow)
        self.actionExport_Excel.setObjectName("actionExport_Excel")
        self.actionExport_Excel.setEnabled(False)
        self.actionGenerate_Report = QtWidgets.QAction(MainWindow)
        self.actionGenerate_Report.setObjectName("actionGenerate_Report")
        self.actionGenerate_Report.setEnabled(False)
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionCut = QtWidgets.QAction(MainWindow)
        self.actionCut.setObjectName("actionCut")
        self.actionCopy = QtWidgets.QAction(MainWindow)
        self.actionCopy.setObjectName("actionCopy")
        self.actionPaste = QtWidgets.QAction(MainWindow)
        self.actionPaste.setObjectName("actionPaste")
        self.actionDelete = QtWidgets.QAction(MainWindow)
        self.actionDelete.setObjectName("actionDelete")
        self.actionUndo = QtWidgets.QAction(MainWindow)
        self.actionUndo.setObjectName("actionUndo")
        self.actionRedo = QtWidgets.QAction(MainWindow)
        self.actionRedo.setObjectName("actionRedo")
        self.actionFind = QtWidgets.QAction(MainWindow)
        self.actionFind.setObjectName("actionFind")
        self.actionSelect_All = QtWidgets.QAction(MainWindow)
        self.actionSelect_All.setObjectName("actionSelect_All")
        self.actionConfigure_Test = QtWidgets.QAction(MainWindow)
        self.actionConfigure_Test.setObjectName("actionConfigure_Test")
        self.actionConnect_to_VNA = QtWidgets.QAction(MainWindow)
        self.actionConnect_to_VNA.setObjectName("actionConnect_to_VNA")
        self.actionConfigure_Reports = QtWidgets.QAction(MainWindow)
        self.actionConfigure_Reports.setObjectName("actionConfigure_Reports")
        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.actionTest = QtWidgets.QAction(MainWindow)
        self.actionTest.setObjectName("actionTest")
        self.actionToolbar_Import_SnP = QtWidgets.QAction(MainWindow)
        self.actionToolbar_Import_SnP.setCheckable(False)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/import.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionToolbar_Import_SnP.setIcon(icon)
        self.actionToolbar_Import_SnP.setObjectName("actionToolbar_Import_SnP")
        self.actionNew_Project = QtWidgets.QAction(MainWindow)
        self.actionNew_Project.setCheckable(False)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/new_project.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.actionNew_Project.setIcon(icon1)
        self.actionNew_Project.setObjectName("actionNew_Project")
        self.actionConnect = QtWidgets.QAction(MainWindow)
        self.actionConnect.setObjectName("actionConnect")
        self.actionWho_am_I = QtWidgets.QAction(MainWindow)
        self.actionWho_am_I.setEnabled(False)
        self.actionWho_am_I.setObjectName("actionWho_am_I")
        self.actionMeasure = QtWidgets.QAction(MainWindow)
        self.actionMeasure.setEnabled(False)
        self.actionMeasure.setObjectName("actionMeasure")
        self.actionCalibrate = QtWidgets.QAction(MainWindow)
        self.actionCalibrate.setEnabled(False)
        self.actionCalibrate.setObjectName("actionCalibrate")
        self.actionDisconnect = QtWidgets.QAction(MainWindow)
        self.actionDisconnect.setEnabled(False)
        self.actionDisconnect.setObjectName("actionDisconnect")
        self.actionRun = QtWidgets.QAction(MainWindow)
        self.actionRun.setEnabled(False)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icons/run.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon2.addPixmap(QtGui.QPixmap(":/icons/run_disabled.png"), QtGui.QIcon.Disabled, QtGui.QIcon.Off)
        icon2.addPixmap(QtGui.QPixmap(":/icons/run_disabled.png"), QtGui.QIcon.Disabled, QtGui.QIcon.On)
        self.actionRun.setIcon(icon2)
        self.actionRun.setObjectName("actionRun")
        self.actionCalibrate_2 = QtWidgets.QAction(MainWindow)
        self.actionCalibrate_2.setEnabled(False)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/icons/calibrate.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon3.addPixmap(QtGui.QPixmap(":/icons/calibrate_disabled.png"), QtGui.QIcon.Disabled, QtGui.QIcon.Off)
        icon3.addPixmap(QtGui.QPixmap(":/icons/calibrate_disabled.png"), QtGui.QIcon.Disabled, QtGui.QIcon.On)
        self.actionCalibrate_2.setIcon(icon3)
        self.actionCalibrate_2.setObjectName("actionCalibrate_2")
        self.actionAlien = QtWidgets.QAction(MainWindow)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/icons/alien.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionAlien.setIcon(icon4)
        self.actionAlien.setObjectName("actionAlien")
        self.actionDeembed = QtWidgets.QAction(MainWindow)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/icons/deembed.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionDeembed.setIcon(icon5)
        self.actionDeembed.setObjectName("actionDeembed")
        self.actionExport_PDF = QtWidgets.QAction(MainWindow)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/icons/ExportPDF.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionExport_PDF.setIcon(icon6)
        self.actionExport_PDF.setObjectName("actionExport_PDF")
        self.actionExport_Excel_2 = QtWidgets.QAction(MainWindow)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/icons/ExportExcel.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionExport_Excel_2.setIcon(icon7)
        self.actionExport_Excel_2.setObjectName("actionExport_Excel_2")
        self.toolBar.addAction(self.actionNew_Project)
        self.toolBar.addAction(self.actionToolbar_Import_SnP)
        self.toolBar.addAction(self.actionRun)
        self.toolBar.addAction(self.actionCalibrate_2)
        self.toolBar.addAction(self.actionAlien)
        self.toolBar.addAction(self.actionDeembed)
        self.toolBar.addAction(self.actionExport_PDF)
        self.toolBar.addAction(self.actionExport_Excel_2)
        self.menuFile.addAction(self.actionImport_Project)
        self.menuFile.addAction(self.actionImport_SnP)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionSave_Project)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExport_Excel)
        self.menuFile.addAction(self.actionGenerate_Report)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExit)
        self.menuFile.addSeparator()
        self.menuEdit.addAction(self.actionCut)
        self.menuEdit.addAction(self.actionCopy)
        self.menuEdit.addAction(self.actionPaste)
        self.menuEdit.addAction(self.actionDelete)
        self.menuEdit.addSeparator()
        self.menuEdit.addAction(self.actionUndo)
        self.menuEdit.addAction(self.actionRedo)
        self.menuEdit.addSeparator()
        self.menuEdit.addAction(self.actionSelect_All)
        self.menuEdit.addSeparator()
        self.menuEdit.addAction(self.actionFind)
        self.menuSettings.addAction(self.actionConfigure_Test)
        self.menuSettings.addAction(self.actionConfigure_Reports)
        self.menuSettings.addSeparator()
        self.menuSettings.addAction(self.actionTest)
        self.menuVNA.addAction(self.actionConnect)
        self.menuVNA.addAction(self.actionDisconnect)
        self.menuVNA.addSeparator()
        self.menuVNA.addAction(self.actionMeasure)
        self.menuVNA.addAction(self.actionCalibrate)
        self.menuVNA.addSeparator()
        self.menuVNA.addAction(self.actionWho_am_I)
        self.menuBar.addAction(self.menuFile.menuAction())
        self.menuBar.addAction(self.menuEdit.menuAction())
        self.menuBar.addAction(self.menuVNA.menuAction())
        self.menuBar.addAction(self.menuSettings.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Belden Network Analyzer Software "))
        self.param_tabs.setTabText(self.param_tabs.indexOf(self.tab), _translate("MainWindow", "Page"))
        self.toolBar2.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar_2"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuEdit.setTitle(_translate("MainWindow", "Edit"))
        self.menuSettings.setTitle(_translate("MainWindow", "Settings"))
        self.menuVNA.setTitle(_translate("MainWindow", "VNA"))
        self.actionImport_SnP.setText(_translate("MainWindow", "Import SnP"))
        self.actionImport_Project.setText(_translate("MainWindow", "Import Project"))
        self.actionSave_Project.setText(_translate("MainWindow", "Save Project"))
        self.actionExport_Excel.setText(_translate("MainWindow", "Export Excel"))
        self.actionGenerate_Report.setText(_translate("MainWindow", "Generate Report"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionCut.setText(_translate("MainWindow", "Cut"))
        self.actionCopy.setText(_translate("MainWindow", "Copy"))
        self.actionPaste.setText(_translate("MainWindow", "Paste"))
        self.actionDelete.setText(_translate("MainWindow", "Delete"))
        self.actionUndo.setText(_translate("MainWindow", "Undo"))
        self.actionRedo.setText(_translate("MainWindow", "Redo"))
        self.actionFind.setText(_translate("MainWindow", "Find"))
        self.actionSelect_All.setText(_translate("MainWindow", "Select All"))
        self.actionConfigure_Test.setText(_translate("MainWindow", "Configure Test"))
        self.actionConnect_to_VNA.setText(_translate("MainWindow", "Connect"))
        self.actionConfigure_Reports.setText(_translate("MainWindow", "Configure Reports"))
        self.actionAbout.setText(_translate("MainWindow", "About"))
        self.actionTest.setText(_translate("MainWindow", "Test"))
        self.actionToolbar_Import_SnP.setText(_translate("MainWindow", "Import Snp"))
        self.actionToolbar_Import_SnP.setToolTip(_translate("MainWindow", "Import SnP file"))
        self.actionNew_Project.setText(_translate("MainWindow", "New Project"))
        self.actionNew_Project.setToolTip(_translate("MainWindow", "Create New Project"))
        self.actionConnect.setText(_translate("MainWindow", "Connect"))
        self.actionWho_am_I.setText(_translate("MainWindow", "Who am I ?"))
        self.actionMeasure.setText(_translate("MainWindow", "Measure"))
        self.actionCalibrate.setText(_translate("MainWindow", "Calibrate"))
        self.actionDisconnect.setText(_translate("MainWindow", "Disconnect"))
        self.actionRun.setText(_translate("MainWindow", "Run"))
        self.actionCalibrate_2.setText(_translate("MainWindow", "Calibrate"))
        self.actionAlien.setText(_translate("MainWindow", "Alien"))
        self.actionAlien.setToolTip(_translate("MainWindow", "Alien"))
        self.actionDeembed.setText(_translate("MainWindow", "Deembed"))
        self.actionDeembed.setToolTip(_translate("MainWindow", "Deembed"))
        self.actionExport_PDF.setText(_translate("MainWindow", "Export PDF Repport"))
        self.actionExport_Excel_2.setText(_translate("MainWindow", "Export Excel Repport"))
        self.actionExport_Excel_2.setToolTip(_translate("MainWindow", "Export Excel Repport"))

import snpanalyzer.gui.ressources.icons  

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

