# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/nyko/python/pyui-generator/pyuiGenerator_app/ui/dialogAddMulti.ui'
#
# Created: Thu Oct 11 21:44:54 2012
#      by: pyside-uic 0.2.13 running on PySide 1.1.0
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_DialogAddMulti(object):
    def setupUi(self, DialogAddMulti):
        DialogAddMulti.setObjectName("DialogAddMulti")
        DialogAddMulti.resize(436, 107)
        self.gridLayout = QtGui.QGridLayout(DialogAddMulti)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtGui.QLabel(DialogAddMulti)
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)
        self.lineEditOutDir = QtGui.QLineEdit(DialogAddMulti)
        self.lineEditOutDir.setMinimumSize(QtCore.QSize(300, 0))
        self.lineEditOutDir.setReadOnly(False)
        self.lineEditOutDir.setObjectName("lineEditOutDir")
        self.gridLayout.addWidget(self.lineEditOutDir, 1, 1, 1, 1)
        self.btnOutDir = QtGui.QToolButton(DialogAddMulti)
        self.btnOutDir.setText("...")
        self.btnOutDir.setObjectName("btnOutDir")
        self.gridLayout.addWidget(self.btnOutDir, 1, 2, 1, 1)
        self.buttonBox = QtGui.QDialogButtonBox(DialogAddMulti)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout.addWidget(self.buttonBox, 3, 0, 1, 3)
        self.label_2 = QtGui.QLabel(DialogAddMulti)
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)
        self.lineEditInFile = QtGui.QLineEdit(DialogAddMulti)
        self.lineEditInFile.setReadOnly(True)
        self.lineEditInFile.setObjectName("lineEditInFile")
        self.gridLayout.addWidget(self.lineEditInFile, 0, 1, 1, 1)
        self.btnInFile = QtGui.QToolButton(DialogAddMulti)
        self.btnInFile.setText("...")
        self.btnInFile.setObjectName("btnInFile")
        self.gridLayout.addWidget(self.btnInFile, 0, 2, 1, 1)

        self.retranslateUi(DialogAddMulti)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), DialogAddMulti.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), DialogAddMulti.reject)
        QtCore.QMetaObject.connectSlotsByName(DialogAddMulti)

    def retranslateUi(self, DialogAddMulti):
        DialogAddMulti.setWindowTitle(QtGui.QApplication.translate("DialogAddMulti", "Add several files", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("DialogAddMulti", "Ouput folder:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("DialogAddMulti", "Input files:", None, QtGui.QApplication.UnicodeUTF8))

