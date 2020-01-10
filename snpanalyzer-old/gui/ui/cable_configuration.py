# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './ui/cable_configuration.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_form(object):
    def setupUi(self, form):
        form.setObjectName("form")
        form.resize(400, 400)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(form.sizePolicy().hasHeightForWidth())
        form.setSizePolicy(sizePolicy)
        form.setMinimumSize(QtCore.QSize(400, 400))
        form.setMaximumSize(QtCore.QSize(400, 400))
        form.setBaseSize(QtCore.QSize(400, 400))
        self.verticalLayout = QtWidgets.QVBoxLayout(form)
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.verticalLayout.setObjectName("verticalLayout")
        self.presetHorizontalLayout = QtWidgets.QHBoxLayout()
        self.presetHorizontalLayout.setObjectName("presetHorizontalLayout")
        self.presetsLabel = QtWidgets.QLabel(form)
        self.presetsLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.presetsLabel.setObjectName("presetsLabel")
        self.presetHorizontalLayout.addWidget(self.presetsLabel)
        self.presetComboBox = QtWidgets.QComboBox(form)
        self.presetComboBox.setObjectName("presetComboBox")
        self.presetHorizontalLayout.addWidget(self.presetComboBox)
        self.presetAddPushButton = QtWidgets.QPushButton(form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.presetAddPushButton.sizePolicy().hasHeightForWidth())
        self.presetAddPushButton.setSizePolicy(sizePolicy)
        self.presetAddPushButton.setMinimumSize(QtCore.QSize(32, 32))
        self.presetAddPushButton.setMaximumSize(QtCore.QSize(32, 32))
        self.presetAddPushButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/plus-circle.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.presetAddPushButton.setIcon(icon)
        self.presetAddPushButton.setFlat(True)
        self.presetAddPushButton.setObjectName("presetAddPushButton")
        self.presetHorizontalLayout.addWidget(self.presetAddPushButton)
        self.presetRemovePushButton = QtWidgets.QPushButton(form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.presetRemovePushButton.sizePolicy().hasHeightForWidth())
        self.presetRemovePushButton.setSizePolicy(sizePolicy)
        self.presetRemovePushButton.setMinimumSize(QtCore.QSize(32, 32))
        self.presetRemovePushButton.setMaximumSize(QtCore.QSize(32, 32))
        self.presetRemovePushButton.setBaseSize(QtCore.QSize(0, 0))
        self.presetRemovePushButton.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/minus-circle.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.presetRemovePushButton.setIcon(icon1)
        self.presetRemovePushButton.setFlat(True)
        self.presetRemovePushButton.setObjectName("presetRemovePushButton")
        self.presetHorizontalLayout.addWidget(self.presetRemovePushButton)
        self.verticalLayout.addLayout(self.presetHorizontalLayout)
        spacerItem = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.pair36VerticalLayout = QtWidgets.QVBoxLayout()
        self.pair36VerticalLayout.setObjectName("pair36VerticalLayout")
        self.pair36Label = QtWidgets.QLabel(form)
        self.pair36Label.setAlignment(QtCore.Qt.AlignCenter)
        self.pair36Label.setObjectName("pair36Label")
        self.pair36VerticalLayout.addWidget(self.pair36Label)
        self.pair36NameEdit = QtWidgets.QLineEdit(form)
        self.pair36NameEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.pair36NameEdit.setObjectName("pair36NameEdit")
        self.pair36VerticalLayout.addWidget(self.pair36NameEdit)
        self.gridLayout.addLayout(self.pair36VerticalLayout, 3, 1, 1, 1)
        self.inputPortsLabel = QtWidgets.QLabel(form)
        self.inputPortsLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.inputPortsLabel.setObjectName("inputPortsLabel")
        self.gridLayout.addWidget(self.inputPortsLabel, 0, 0, 1, 1)
        self.outputPortsLabel = QtWidgets.QLabel(form)
        self.outputPortsLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.outputPortsLabel.setObjectName("outputPortsLabel")
        self.gridLayout.addWidget(self.outputPortsLabel, 0, 2, 1, 1)
        self.pair12VerticalLayout = QtWidgets.QVBoxLayout()
        self.pair12VerticalLayout.setObjectName("pair12VerticalLayout")
        self.pair12Label = QtWidgets.QLabel(form)
        self.pair12Label.setAlignment(QtCore.Qt.AlignCenter)
        self.pair12Label.setObjectName("pair12Label")
        self.pair12VerticalLayout.addWidget(self.pair12Label)
        self.pair12NameEdit = QtWidgets.QLineEdit(form)
        self.pair12NameEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.pair12NameEdit.setObjectName("pair12NameEdit")
        self.pair12VerticalLayout.addWidget(self.pair12NameEdit)
        self.gridLayout.addLayout(self.pair12VerticalLayout, 1, 1, 1, 1)
        self.pair78VerticalLayout = QtWidgets.QVBoxLayout()
        self.pair78VerticalLayout.setObjectName("pair78VerticalLayout")
        self.pair78Label = QtWidgets.QLabel(form)
        self.pair78Label.setAlignment(QtCore.Qt.AlignCenter)
        self.pair78Label.setObjectName("pair78Label")
        self.pair78VerticalLayout.addWidget(self.pair78Label)
        self.pair78NameEdit = QtWidgets.QLineEdit(form)
        self.pair78NameEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.pair78NameEdit.setObjectName("pair78NameEdit")
        self.pair78VerticalLayout.addWidget(self.pair78NameEdit)
        self.gridLayout.addLayout(self.pair78VerticalLayout, 7, 1, 1, 1)
        self.pair45VerticalLayout = QtWidgets.QVBoxLayout()
        self.pair45VerticalLayout.setObjectName("pair45VerticalLayout")
        self.pair45Label = QtWidgets.QLabel(form)
        self.pair45Label.setAlignment(QtCore.Qt.AlignCenter)
        self.pair45Label.setObjectName("pair45Label")
        self.pair45VerticalLayout.addWidget(self.pair45Label)
        self.pair45NameEdit = QtWidgets.QLineEdit(form)
        self.pair45NameEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.pair45NameEdit.setObjectName("pair45NameEdit")
        self.pair45VerticalLayout.addWidget(self.pair45NameEdit)
        self.gridLayout.addLayout(self.pair45VerticalLayout, 5, 1, 1, 1)
        self.inputPort1VerticalLayout = QtWidgets.QVBoxLayout()
        self.inputPort1VerticalLayout.setObjectName("inputPort1VerticalLayout")
        self.inputPort1ComboBox = QtWidgets.QComboBox(form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.inputPort1ComboBox.sizePolicy().hasHeightForWidth())
        self.inputPort1ComboBox.setSizePolicy(sizePolicy)
        self.inputPort1ComboBox.setObjectName("inputPort1ComboBox")
        self.inputPort1VerticalLayout.addWidget(self.inputPort1ComboBox)
        self.inputPort1LineEdit = QtWidgets.QLineEdit(form)
        self.inputPort1LineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.inputPort1LineEdit.setObjectName("inputPort1LineEdit")
        self.inputPort1VerticalLayout.addWidget(self.inputPort1LineEdit)
        self.gridLayout.addLayout(self.inputPort1VerticalLayout, 1, 0, 1, 1)
        self.inputPort2VerticalLayout = QtWidgets.QVBoxLayout()
        self.inputPort2VerticalLayout.setObjectName("inputPort2VerticalLayout")
        self.inputPort2ComboBox = QtWidgets.QComboBox(form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.inputPort2ComboBox.sizePolicy().hasHeightForWidth())
        self.inputPort2ComboBox.setSizePolicy(sizePolicy)
        self.inputPort2ComboBox.setObjectName("inputPort2ComboBox")
        self.inputPort2VerticalLayout.addWidget(self.inputPort2ComboBox)
        self.inputPort2LineEdit = QtWidgets.QLineEdit(form)
        self.inputPort2LineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.inputPort2LineEdit.setObjectName("inputPort2LineEdit")
        self.inputPort2VerticalLayout.addWidget(self.inputPort2LineEdit)
        self.gridLayout.addLayout(self.inputPort2VerticalLayout, 3, 0, 1, 1)
        self.inputPort3VerticalLayout = QtWidgets.QVBoxLayout()
        self.inputPort3VerticalLayout.setObjectName("inputPort3VerticalLayout")
        self.inputPort3ComboBox = QtWidgets.QComboBox(form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.inputPort3ComboBox.sizePolicy().hasHeightForWidth())
        self.inputPort3ComboBox.setSizePolicy(sizePolicy)
        self.inputPort3ComboBox.setObjectName("inputPort3ComboBox")
        self.inputPort3VerticalLayout.addWidget(self.inputPort3ComboBox)
        self.inputPort3LineEdit = QtWidgets.QLineEdit(form)
        self.inputPort3LineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.inputPort3LineEdit.setObjectName("inputPort3LineEdit")
        self.inputPort3VerticalLayout.addWidget(self.inputPort3LineEdit)
        self.gridLayout.addLayout(self.inputPort3VerticalLayout, 5, 0, 1, 1)
        self.inputPort4VerticalLayout = QtWidgets.QVBoxLayout()
        self.inputPort4VerticalLayout.setObjectName("inputPort4VerticalLayout")
        self.inputPort4ComboBox = QtWidgets.QComboBox(form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.inputPort4ComboBox.sizePolicy().hasHeightForWidth())
        self.inputPort4ComboBox.setSizePolicy(sizePolicy)
        self.inputPort4ComboBox.setObjectName("inputPort4ComboBox")
        self.inputPort4VerticalLayout.addWidget(self.inputPort4ComboBox)
        self.inputPort4LineEdit = QtWidgets.QLineEdit(form)
        self.inputPort4LineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.inputPort4LineEdit.setObjectName("inputPort4LineEdit")
        self.inputPort4VerticalLayout.addWidget(self.inputPort4LineEdit)
        self.gridLayout.addLayout(self.inputPort4VerticalLayout, 7, 0, 1, 1)
        self.outputPort1VerticalLayout = QtWidgets.QVBoxLayout()
        self.outputPort1VerticalLayout.setObjectName("outputPort1VerticalLayout")
        self.outputPort1ComboBox = QtWidgets.QComboBox(form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.outputPort1ComboBox.sizePolicy().hasHeightForWidth())
        self.outputPort1ComboBox.setSizePolicy(sizePolicy)
        self.outputPort1ComboBox.setObjectName("outputPort1ComboBox")
        self.outputPort1VerticalLayout.addWidget(self.outputPort1ComboBox)
        self.outputPort1LineEdit = QtWidgets.QLineEdit(form)
        self.outputPort1LineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.outputPort1LineEdit.setObjectName("outputPort1LineEdit")
        self.outputPort1VerticalLayout.addWidget(self.outputPort1LineEdit)
        self.gridLayout.addLayout(self.outputPort1VerticalLayout, 1, 2, 1, 1)
        self.outputPort2VerticalLayout = QtWidgets.QVBoxLayout()
        self.outputPort2VerticalLayout.setObjectName("outputPort2VerticalLayout")
        self.outputPort2ComboBox = QtWidgets.QComboBox(form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.outputPort2ComboBox.sizePolicy().hasHeightForWidth())
        self.outputPort2ComboBox.setSizePolicy(sizePolicy)
        self.outputPort2ComboBox.setObjectName("outputPort2ComboBox")
        self.outputPort2VerticalLayout.addWidget(self.outputPort2ComboBox)
        self.outputPort2LineEdit = QtWidgets.QLineEdit(form)
        self.outputPort2LineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.outputPort2LineEdit.setObjectName("outputPort2LineEdit")
        self.outputPort2VerticalLayout.addWidget(self.outputPort2LineEdit)
        self.gridLayout.addLayout(self.outputPort2VerticalLayout, 3, 2, 1, 1)
        self.outputPort3VerticalLayout = QtWidgets.QVBoxLayout()
        self.outputPort3VerticalLayout.setObjectName("outputPort3VerticalLayout")
        self.outputPort3ComboBox = QtWidgets.QComboBox(form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.outputPort3ComboBox.sizePolicy().hasHeightForWidth())
        self.outputPort3ComboBox.setSizePolicy(sizePolicy)
        self.outputPort3ComboBox.setObjectName("outputPort3ComboBox")
        self.outputPort3VerticalLayout.addWidget(self.outputPort3ComboBox)
        self.outputPort3LineEdit = QtWidgets.QLineEdit(form)
        self.outputPort3LineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.outputPort3LineEdit.setObjectName("outputPort3LineEdit")
        self.outputPort3VerticalLayout.addWidget(self.outputPort3LineEdit)
        self.gridLayout.addLayout(self.outputPort3VerticalLayout, 5, 2, 1, 1)
        self.outputPort4VerticalLayout = QtWidgets.QVBoxLayout()
        self.outputPort4VerticalLayout.setObjectName("outputPort4VerticalLayout")
        self.outputPort4ComboBox = QtWidgets.QComboBox(form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.outputPort4ComboBox.sizePolicy().hasHeightForWidth())
        self.outputPort4ComboBox.setSizePolicy(sizePolicy)
        self.outputPort4ComboBox.setObjectName("outputPort4ComboBox")
        self.outputPort4VerticalLayout.addWidget(self.outputPort4ComboBox)
        self.outputPort4LineEdit = QtWidgets.QLineEdit(form)
        self.outputPort4LineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.outputPort4LineEdit.setObjectName("outputPort4LineEdit")
        self.outputPort4VerticalLayout.addWidget(self.outputPort4LineEdit)
        self.gridLayout.addLayout(self.outputPort4VerticalLayout, 7, 2, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem1, 2, 1, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem2, 4, 1, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem3, 6, 1, 1, 1)
        self.gridLayout.setColumnMinimumWidth(1, 200)
        self.verticalLayout.addLayout(self.gridLayout)
        spacerItem4 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem4)
        self.bottomHorizontalLayout = QtWidgets.QHBoxLayout()
        self.bottomHorizontalLayout.setObjectName("bottomHorizontalLayout")
        self.hideNamesCheckBox = QtWidgets.QCheckBox(form)
        self.hideNamesCheckBox.setObjectName("hideNamesCheckBox")
        self.bottomHorizontalLayout.addWidget(self.hideNamesCheckBox)
        self.buttonBox = QtWidgets.QDialogButtonBox(form)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.bottomHorizontalLayout.addWidget(self.buttonBox)
        self.verticalLayout.addLayout(self.bottomHorizontalLayout)

        self.retranslateUi(form)
        QtCore.QMetaObject.connectSlotsByName(form)

    def retranslateUi(self, form):
        _translate = QtCore.QCoreApplication.translate
        form.setWindowTitle(_translate("form", "Form"))
        self.presetsLabel.setText(_translate("form", "Presets"))
        self.pair36Label.setText(_translate("form", "Pair 36"))
        self.inputPortsLabel.setText(_translate("form", "Input Ports"))
        self.outputPortsLabel.setText(_translate("form", "Output Ports"))
        self.pair12Label.setText(_translate("form", "Pair 12"))
        self.pair78Label.setText(_translate("form", "Pair 78"))
        self.pair45Label.setText(_translate("form", "Pair 45"))
        self.hideNamesCheckBox.setText(_translate("form", "Hide Names"))

from snpanalyzer.gui.ressources import icons_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    form = QtWidgets.QWidget()
    ui = Ui_form()
    ui.setupUi(form)
    form.show()
    sys.exit(app.exec_())

