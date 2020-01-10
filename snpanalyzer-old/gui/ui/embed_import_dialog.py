# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UIs\embedImportDialog.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_EmbedImportDialog(object):
    def setupUi(self, EmbedImportDialog):
        EmbedImportDialog.setObjectName("EmbedImportDialog")
        EmbedImportDialog.resize(452, 345)
        self.buttonBox = QtWidgets.QDialogButtonBox(EmbedImportDialog)
        self.buttonBox.setGeometry(QtCore.QRect(30, 300, 401, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.formLayoutWidget = QtWidgets.QWidget(EmbedImportDialog)
        self.formLayoutWidget.setGeometry(QtCore.QRect(10, 30, 431, 83))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.openBtn = QtWidgets.QPushButton(self.formLayoutWidget)
        self.openBtn.setObjectName("openBtn")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.openBtn)
        self.shortBtn = QtWidgets.QPushButton(self.formLayoutWidget)
        self.shortBtn.setObjectName("shortBtn")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.shortBtn)
        self.shortLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.shortLabel.setText("")
        self.shortLabel.setObjectName("shortLabel")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.shortLabel)
        self.openLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.openLabel.setText("")
        self.openLabel.setObjectName("openLabel")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.openLabel)
        self.revBox = QtWidgets.QCheckBox(self.formLayoutWidget)
        self.revBox.setObjectName("revBox")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.revBox)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.cat5eButton = QtWidgets.QRadioButton(self.formLayoutWidget)
        self.cat5eButton.setAutoExclusive(False)
        self.cat5eButton.setObjectName("cat5eButton")
        self.horizontalLayout.addWidget(self.cat5eButton)
        self.cat6Button = QtWidgets.QRadioButton(self.formLayoutWidget)
        self.cat6Button.setChecked(True)
        self.cat6Button.setAutoExclusive(False)
        self.cat6Button.setObjectName("cat6Button")
        self.horizontalLayout.addWidget(self.cat6Button)
        self.formLayout.setLayout(0, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout)
        self.formLayoutWidget_2 = QtWidgets.QWidget(EmbedImportDialog)
        self.formLayoutWidget_2.setGeometry(QtCore.QRect(10, 120, 431, 180))
        self.formLayoutWidget_2.setObjectName("formLayoutWidget_2")
        self.formLayout_2 = QtWidgets.QFormLayout(self.formLayoutWidget_2)
        self.formLayout_2.setContentsMargins(0, 0, 0, 0)
        self.formLayout_2.setObjectName("formLayout_2")
        self.loadBtn = QtWidgets.QPushButton(self.formLayoutWidget_2)
        self.loadBtn.setObjectName("loadBtn")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.loadBtn)
        self.loadLabel = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.loadLabel.setText("")
        self.loadLabel.setObjectName("loadLabel")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.loadLabel)
        self.sJ124578Label = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.sJ124578Label.setObjectName("sJ124578Label")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.sJ124578Label)
        self.sJ12LineEdit = QtWidgets.QLineEdit(self.formLayoutWidget_2)
        self.sJ12LineEdit.setObjectName("sJ12LineEdit")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.sJ12LineEdit)
        self.sJ36Label = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.sJ36Label.setObjectName("sJ36Label")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.sJ36Label)
        self.sJ36LineEdit = QtWidgets.QLineEdit(self.formLayoutWidget_2)
        self.sJ36LineEdit.setObjectName("sJ36LineEdit")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.sJ36LineEdit)
        self.thruCalibLabel = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.thruCalibLabel.setObjectName("thruCalibLabel")
        self.formLayout_2.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.thruCalibLabel)
        self.thruCalibLineEdit = QtWidgets.QLineEdit(self.formLayoutWidget_2)
        self.thruCalibLineEdit.setObjectName("thruCalibLineEdit")
        self.formLayout_2.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.thruCalibLineEdit)
        self.plugBtn = QtWidgets.QPushButton(self.formLayoutWidget_2)
        self.plugBtn.setObjectName("plugBtn")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.plugBtn)
        self.plugLabel = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.plugLabel.setText("")
        self.plugLabel.setObjectName("plugLabel")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.plugLabel)

        self.retranslateUi(EmbedImportDialog)
        self.buttonBox.accepted.connect(EmbedImportDialog.accept)
        self.buttonBox.rejected.connect(EmbedImportDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(EmbedImportDialog)

    def retranslateUi(self, EmbedImportDialog):
        _translate = QtCore.QCoreApplication.translate
        EmbedImportDialog.setWindowTitle(_translate("EmbedImportDialog", "Import Embedding SNPs"))
        self.openBtn.setText(_translate("EmbedImportDialog", "Import Open"))
        self.shortBtn.setText(_translate("EmbedImportDialog", "Import Short"))
        self.revBox.setText(_translate("EmbedImportDialog", "Reverse ?"))
        self.cat5eButton.setText(_translate("EmbedImportDialog", "CAT5e"))
        self.cat6Button.setText(_translate("EmbedImportDialog", "CAT6/CAT6A"))
        self.loadBtn.setText(_translate("EmbedImportDialog", "Import Load"))
        self.sJ124578Label.setText(_translate("EmbedImportDialog", "SJ 12,45,78"))
        self.sJ36Label.setText(_translate("EmbedImportDialog", "SJ 36"))
        self.thruCalibLabel.setText(_translate("EmbedImportDialog", "Thru Calib"))
        self.plugBtn.setText(_translate("EmbedImportDialog", "Import Plug"))

