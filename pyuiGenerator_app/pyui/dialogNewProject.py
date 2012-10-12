# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/nyko/python/pyui-generator/pyuiGenerator_app/ui/dialogNewProject.ui'
#
# Created: Thu Oct 11 21:44:54 2012
#      by: pyside-uic 0.2.13 running on PySide 1.1.0
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_DialogNewProject(object):
    def setupUi(self, DialogNewProject):
        DialogNewProject.setObjectName("DialogNewProject")
        DialogNewProject.resize(312, 132)
        self.verticalLayout = QtGui.QVBoxLayout(DialogNewProject)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtGui.QLabel(DialogNewProject)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.lineEditName = QtGui.QLineEdit(DialogNewProject)
        self.lineEditName.setObjectName("lineEditName")
        self.horizontalLayout.addWidget(self.lineEditName)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.radioButtonPyside = QtGui.QRadioButton(DialogNewProject)
        self.radioButtonPyside.setText("pyside")
        self.radioButtonPyside.setChecked(True)
        self.radioButtonPyside.setObjectName("radioButtonPyside")
        self.verticalLayout.addWidget(self.radioButtonPyside)
        self.radioButtonPyqt = QtGui.QRadioButton(DialogNewProject)
        self.radioButtonPyqt.setText("pyqt")
        self.radioButtonPyqt.setChecked(False)
        self.radioButtonPyqt.setObjectName("radioButtonPyqt")
        self.verticalLayout.addWidget(self.radioButtonPyqt)
        self.buttonBox = QtGui.QDialogButtonBox(DialogNewProject)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(DialogNewProject)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), DialogNewProject.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), DialogNewProject.reject)
        QtCore.QMetaObject.connectSlotsByName(DialogNewProject)

    def retranslateUi(self, DialogNewProject):
        DialogNewProject.setWindowTitle(QtGui.QApplication.translate("DialogNewProject", "New project", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("DialogNewProject", "Project name:", None, QtGui.QApplication.UnicodeUTF8))

