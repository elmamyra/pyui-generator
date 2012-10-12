# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/nyko/python/pyui-generator/pyuiGenerator_app/ui/dialogNewItem.ui'
#
# Created: Thu Oct 11 21:44:54 2012
#      by: pyside-uic 0.2.13 running on PySide 1.1.0
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_DialogNewItem(object):
    def setupUi(self, DialogNewItem):
        DialogNewItem.setObjectName("DialogNewItem")
        DialogNewItem.resize(404, 144)
        self.verticalLayout = QtGui.QVBoxLayout(DialogNewItem)
        self.verticalLayout.setObjectName("verticalLayout")
        self.formLayout = QtGui.QFormLayout()
        self.formLayout.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setLabelAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.formLayout.setObjectName("formLayout")
        self.label = QtGui.QLabel(DialogNewItem)
        self.label.setObjectName("label")
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.label)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.lineEditIn = QtGui.QLineEdit(DialogNewItem)
        self.lineEditIn.setMinimumSize(QtCore.QSize(300, 0))
        self.lineEditIn.setObjectName("lineEditIn")
        self.horizontalLayout_2.addWidget(self.lineEditIn)
        self.btnIn = QtGui.QToolButton(DialogNewItem)
        self.btnIn.setText("...")
        self.btnIn.setObjectName("btnIn")
        self.horizontalLayout_2.addWidget(self.btnIn)
        self.formLayout.setLayout(1, QtGui.QFormLayout.FieldRole, self.horizontalLayout_2)
        self.label_2 = QtGui.QLabel(DialogNewItem)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.label_2)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lineEditOut = QtGui.QLineEdit(DialogNewItem)
        self.lineEditOut.setObjectName("lineEditOut")
        self.horizontalLayout.addWidget(self.lineEditOut)
        self.btnOut = QtGui.QToolButton(DialogNewItem)
        self.btnOut.setText("...")
        self.btnOut.setObjectName("btnOut")
        self.horizontalLayout.addWidget(self.btnOut)
        self.formLayout.setLayout(2, QtGui.QFormLayout.FieldRole, self.horizontalLayout)
        self.label_3 = QtGui.QLabel(DialogNewItem)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.label_3)
        self.lineEditName = QtGui.QLineEdit(DialogNewItem)
        self.lineEditName.setMaximumSize(QtCore.QSize(150, 16777215))
        self.lineEditName.setObjectName("lineEditName")
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.lineEditName)
        self.verticalLayout.addLayout(self.formLayout)
        self.buttonBox = QtGui.QDialogButtonBox(DialogNewItem)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(DialogNewItem)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), DialogNewItem.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), DialogNewItem.reject)
        QtCore.QMetaObject.connectSlotsByName(DialogNewItem)

    def retranslateUi(self, DialogNewItem):
        DialogNewItem.setWindowTitle(QtGui.QApplication.translate("DialogNewItem", "add file", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("DialogNewItem", "input:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("DialogNewItem", "output:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("DialogNewItem", "Name:", None, QtGui.QApplication.UnicodeUTF8))

