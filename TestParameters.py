# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'TestParameters.ui'
#
# Created by: PyQt5 UI code generator 5.10
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_TestParameterDialog(object):
    def setupUi(self, TestParameterDialog):
        TestParameterDialog.setObjectName("TestParameterDialog")
        TestParameterDialog.resize(663, 351)
        self.buttonBox = QtWidgets.QDialogButtonBox(TestParameterDialog)
        self.buttonBox.setGeometry(QtCore.QRect(470, 270, 164, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setCenterButtons(False)
        self.buttonBox.setObjectName("buttonBox")
        self.formLayoutWidget = QtWidgets.QWidget(TestParameterDialog)
        self.formLayoutWidget.setGeometry(QtCore.QRect(370, 30, 261, 221))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.iFBandwidthLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.iFBandwidthLabel.setObjectName("iFBandwidthLabel")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.iFBandwidthLabel)
        self.iFBandwidthLineEdit = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.iFBandwidthLineEdit.setInputMask("")
        self.iFBandwidthLineEdit.setFrame(True)
        self.iFBandwidthLineEdit.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.iFBandwidthLineEdit.setCursorPosition(0)
        self.iFBandwidthLineEdit.setCursorMoveStyle(QtCore.Qt.VisualMoveStyle)
        self.iFBandwidthLineEdit.setObjectName("iFBandwidthLineEdit")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.iFBandwidthLineEdit)
        self.startFrequencyLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.startFrequencyLabel.setObjectName("startFrequencyLabel")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.startFrequencyLabel)
        self.startFrequencyLineEdit = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.startFrequencyLineEdit.setInputMask("")
        self.startFrequencyLineEdit.setObjectName("startFrequencyLineEdit")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.startFrequencyLineEdit)
        self.stopFrequencyLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.stopFrequencyLabel.setObjectName("stopFrequencyLabel")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.stopFrequencyLabel)
        self.stopFrequencyLineEdit = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.stopFrequencyLineEdit.setInputMask("")
        self.stopFrequencyLineEdit.setObjectName("stopFrequencyLineEdit")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.stopFrequencyLineEdit)
        self.numberOfPointsLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.numberOfPointsLabel.setObjectName("numberOfPointsLabel")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.numberOfPointsLabel)
        self.numberOfPointsLineEdit = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.numberOfPointsLineEdit.setInputMask("")
        self.numberOfPointsLineEdit.setObjectName("numberOfPointsLineEdit")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.numberOfPointsLineEdit)
        self.numberOfAverageLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.numberOfAverageLabel.setObjectName("numberOfAverageLabel")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.numberOfAverageLabel)
        self.numberOfAverageLineEdit = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.numberOfAverageLineEdit.setInputMask("")
        self.numberOfAverageLineEdit.setObjectName("numberOfAverageLineEdit")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.numberOfAverageLineEdit)
        self.timeoutLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.timeoutLabel.setObjectName("timeoutLabel")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.timeoutLabel)
        self.timeoutLineEdit = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.timeoutLineEdit.setInputMask("")
        self.timeoutLineEdit.setObjectName("timeoutLineEdit")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.timeoutLineEdit)
        self.formLayoutWidget_2 = QtWidgets.QWidget(TestParameterDialog)
        self.formLayoutWidget_2.setGeometry(QtCore.QRect(20, 30, 351, 181))
        self.formLayoutWidget_2.setObjectName("formLayoutWidget_2")
        self.formLayout_2 = QtWidgets.QFormLayout(self.formLayoutWidget_2)
        self.formLayout_2.setFormAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.formLayout_2.setContentsMargins(0, 0, 0, 0)
        self.formLayout_2.setObjectName("formLayout_2")
        self.testNameLabel_2 = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.testNameLabel_2.setObjectName("testNameLabel_2")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.testNameLabel_2)
        self.testNameLineEdit_2 = QtWidgets.QLineEdit(self.formLayoutWidget_2)
        self.testNameLineEdit_2.setMinimumSize(QtCore.QSize(230, 30))
        self.testNameLineEdit_2.setObjectName("testNameLineEdit_2")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.testNameLineEdit_2)
        self.numberOfPortsLineEdit = QtWidgets.QLineEdit(self.formLayoutWidget_2)
        self.numberOfPortsLineEdit.setMinimumSize(QtCore.QSize(230, 0))
        self.numberOfPortsLineEdit.setObjectName("numberOfPortsLineEdit")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.numberOfPortsLineEdit)
        self.numberOfPortsLabel = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.numberOfPortsLabel.setObjectName("numberOfPortsLabel")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.numberOfPortsLabel)
        self.limitLineEdit_2 = QtWidgets.QLineEdit(self.formLayoutWidget_2)
        self.limitLineEdit_2.setEnabled(False)
        self.limitLineEdit_2.setMinimumSize(QtCore.QSize(230, 0))
        self.limitLineEdit_2.setObjectName("limitLineEdit_2")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.limitLineEdit_2)
        self.limitLabel_2 = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.limitLabel_2.setObjectName("limitLabel_2")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.limitLabel_2)

        self.retranslateUi(TestParameterDialog)
        self.buttonBox.accepted.connect(TestParameterDialog.accept)
        self.buttonBox.rejected.connect(TestParameterDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(TestParameterDialog)

    def retranslateUi(self, TestParameterDialog):
        _translate = QtCore.QCoreApplication.translate
        TestParameterDialog.setWindowTitle(_translate("TestParameterDialog", "Test Parameters"))
        self.iFBandwidthLabel.setText(_translate("TestParameterDialog", "IF Bandwidth (Hz)"))
        self.startFrequencyLabel.setText(_translate("TestParameterDialog", "Start Frequency ()"))
        self.stopFrequencyLabel.setText(_translate("TestParameterDialog", "Stop Frequency"))
        self.numberOfPointsLabel.setText(_translate("TestParameterDialog", "Number of points"))
        self.numberOfAverageLabel.setText(_translate("TestParameterDialog", "Number of average"))
        self.timeoutLabel.setText(_translate("TestParameterDialog", "Timeout"))
        self.testNameLabel_2.setText(_translate("TestParameterDialog", "Test Name"))
        self.numberOfPortsLabel.setText(_translate("TestParameterDialog", "Number of ports"))
        self.limitLabel_2.setText(_translate("TestParameterDialog", "Limit (optional)"))
