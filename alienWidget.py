# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UIs/alienWidget.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(790, 320)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(Form)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout()
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.alienGeneralInfo = QtWidgets.QGroupBox(Form)
        self.alienGeneralInfo.setObjectName("alienGeneralInfo")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.alienGeneralInfo)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.horizontalLayout_4.addLayout(self.horizontalLayout_3)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.alienVictimButton = QtWidgets.QPushButton(self.alienGeneralInfo)
        self.alienVictimButton.setObjectName("alienVictimButton")
        self.verticalLayout.addWidget(self.alienVictimButton)
        self.horizontalLayout_4.addLayout(self.verticalLayout)
        self.verticalLayout_11.addWidget(self.alienGeneralInfo)
        self.verticalLayout_3.addLayout(self.verticalLayout_11)
        self.AlienPlotLayout = QtWidgets.QVBoxLayout()
        self.AlienPlotLayout.setObjectName("AlienPlotLayout")
        self.alienPlots = QtWidgets.QGroupBox(Form)
        self.alienPlots.setObjectName("alienPlots")
        self.gridLayout = QtWidgets.QGridLayout(self.alienPlots)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout_12 = QtWidgets.QVBoxLayout()
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.alienLimitCheck = QtWidgets.QCheckBox(self.alienPlots)
        self.alienLimitCheck.setChecked(True)
        self.alienLimitCheck.setObjectName("alienLimitCheck")
        self.horizontalLayout_7.addWidget(self.alienLimitCheck)
        self.alienAvgLimitCheck = QtWidgets.QCheckBox(self.alienPlots)
        self.alienAvgLimitCheck.setChecked(True)
        self.alienAvgLimitCheck.setObjectName("alienAvgLimitCheck")
        self.horizontalLayout_7.addWidget(self.alienAvgLimitCheck)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem)
        self.verticalLayout_12.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.alien12 = QtWidgets.QCheckBox(self.alienPlots)
        self.alien12.setChecked(True)
        self.alien12.setObjectName("alien12")
        self.horizontalLayout_8.addWidget(self.alien12)
        self.alien36 = QtWidgets.QCheckBox(self.alienPlots)
        self.alien36.setChecked(True)
        self.alien36.setObjectName("alien36")
        self.horizontalLayout_8.addWidget(self.alien36)
        self.alien45 = QtWidgets.QCheckBox(self.alienPlots)
        self.alien45.setChecked(True)
        self.alien45.setObjectName("alien45")
        self.horizontalLayout_8.addWidget(self.alien45)
        self.alien78 = QtWidgets.QCheckBox(self.alienPlots)
        self.alien78.setChecked(True)
        self.alien78.setObjectName("alien78")
        self.horizontalLayout_8.addWidget(self.alien78)
        self.alienAvg = QtWidgets.QCheckBox(self.alienPlots)
        self.alienAvg.setChecked(True)
        self.alienAvg.setObjectName("alienAvg")
        self.horizontalLayout_8.addWidget(self.alienAvg)
        self.verticalLayout_12.addLayout(self.horizontalLayout_8)
        self.gridLayout.addLayout(self.verticalLayout_12, 2, 1, 1, 1)
        self.AlienPlotLayout.addWidget(self.alienPlots)
        self.verticalLayout_3.addLayout(self.AlienPlotLayout)
        self.horizontalLayout.addLayout(self.verticalLayout_3)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.alienDisturbersGroup = QtWidgets.QGroupBox(Form)
        self.alienDisturbersGroup.setObjectName("alienDisturbersGroup")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.alienDisturbersGroup)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.alienDisturbers = QtWidgets.QListWidget(self.alienDisturbersGroup)
        self.alienDisturbers.setObjectName("alienDisturbers")
        self.horizontalLayout_9.addWidget(self.alienDisturbers)
        self.horizontalLayout_6.addWidget(self.alienDisturbersGroup)
        self.horizontalLayout_5.addLayout(self.horizontalLayout_6)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.alienTestTypeGroup = QtWidgets.QGroupBox(Form)
        self.alienTestTypeGroup.setObjectName("alienTestTypeGroup")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.alienTestTypeGroup)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.alienPSANEXT = QtWidgets.QRadioButton(self.alienTestTypeGroup)
        self.alienPSANEXT.setObjectName("alienPSANEXT")
        self.verticalLayout_9.addWidget(self.alienPSANEXT)
        self.alienPSAACRF = QtWidgets.QRadioButton(self.alienTestTypeGroup)
        self.alienPSAACRF.setObjectName("alienPSAACRF")
        self.verticalLayout_9.addWidget(self.alienPSAACRF)
        self.verticalLayout_7.addWidget(self.alienTestTypeGroup)
        self.verticalLayout_4.addLayout(self.verticalLayout_7)
        self.alienEndGroup = QtWidgets.QGroupBox(Form)
        self.alienEndGroup.setObjectName("alienEndGroup")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.alienEndGroup)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.alienEnd1 = QtWidgets.QRadioButton(self.alienEndGroup)
        self.alienEnd1.setObjectName("alienEnd1")
        self.verticalLayout_10.addWidget(self.alienEnd1)
        self.alienEnd2 = QtWidgets.QRadioButton(self.alienEndGroup)
        self.alienEnd2.setObjectName("alienEnd2")
        self.verticalLayout_10.addWidget(self.alienEnd2)
        self.verticalLayout_4.addWidget(self.alienEndGroup)
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.alienRun = QtWidgets.QPushButton(Form)
        self.alienRun.setObjectName("alienRun")
        self.verticalLayout_8.addWidget(self.alienRun)
        self.alienImportSNP = QtWidgets.QPushButton(Form)
        self.alienImportSNP.setObjectName("alienImportSNP")
        self.verticalLayout_8.addWidget(self.alienImportSNP)
        self.verticalLayout_4.addLayout(self.verticalLayout_8)
        self.horizontalLayout_5.addLayout(self.verticalLayout_4)
        self.horizontalLayout.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_2.addLayout(self.horizontalLayout)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.alienGeneralInfo.setTitle(_translate("Form", "General"))
        self.alienVictimButton.setText(_translate("Form", "Victim SNP"))
        self.alienPlots.setTitle(_translate("Form", "Plots"))
        self.alienLimitCheck.setText(_translate("Form", "Limit"))
        self.alienAvgLimitCheck.setText(_translate("Form", "Avg Limit"))
        self.alien12.setText(_translate("Form", "12"))
        self.alien36.setText(_translate("Form", "36"))
        self.alien45.setText(_translate("Form", "45"))
        self.alien78.setText(_translate("Form", "78"))
        self.alienAvg.setText(_translate("Form", "Avg"))
        self.alienDisturbersGroup.setTitle(_translate("Form", "Disturbers"))
        self.alienTestTypeGroup.setTitle(_translate("Form", "Test Type"))
        self.alienPSANEXT.setText(_translate("Form", "PSANEXT"))
        self.alienPSAACRF.setText(_translate("Form", "PSAACRF"))
        self.alienEndGroup.setTitle(_translate("Form", "End"))
        self.alienEnd1.setText(_translate("Form", "End 1"))
        self.alienEnd2.setText(_translate("Form", "End 2"))
        self.alienRun.setText(_translate("Form", "Run Alien "))
        self.alienImportSNP.setText(_translate("Form", "Import Alien SNP"))

