# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/nyko/python/pyui-generator/pyuiGenerator_app/ui/itemWidget.ui'
#
# Created: Thu Oct 11 21:44:54 2012
#      by: pyside-uic 0.2.13 running on PySide 1.1.0
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_ItemWidget(object):
    def setupUi(self, ItemWidget):
        ItemWidget.setObjectName("ItemWidget")
        ItemWidget.resize(311, 35)
        self.verticalLayout = QtGui.QVBoxLayout(ItemWidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setSpacing(4)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btnExec = QtGui.QToolButton(ItemWidget)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icon/exec.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnExec.setIcon(icon)
        self.btnExec.setIconSize(QtCore.QSize(24, 24))
        self.btnExec.setObjectName("btnExec")
        self.horizontalLayout.addWidget(self.btnExec)
        self.labelNom = QtGui.QLabel(ItemWidget)
        self.labelNom.setObjectName("labelNom")
        self.horizontalLayout.addWidget(self.labelNom)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(ItemWidget)
        QtCore.QMetaObject.connectSlotsByName(ItemWidget)

    def retranslateUi(self, ItemWidget):
        ItemWidget.setWindowTitle(QtGui.QApplication.translate("ItemWidget", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.btnExec.setText(QtGui.QApplication.translate("ItemWidget", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.labelNom.setText(QtGui.QApplication.translate("ItemWidget", "nom", None, QtGui.QApplication.UnicodeUTF8))

import resource_rc
