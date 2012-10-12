#!/usr/bin/env python
# -*- coding: utf-8 -*-

## This file is part of the pyui generator project
#Copyright (C) 2012 by elmamyra
#
#This program is free software: you can redistribute it and/or modify
#it under the terms of the GNU General Public License as published by
#the Free Software Foundation, either version 3 of the License, or
#(at your option) any later version.
#
#This program is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#GNU General Public License for more details.
#
#You should have received a copy of the GNU General Public License
#along with this program.  If not, see <http://www.gnu.org/licenses/>.

from PySide.QtCore import *
from PySide.QtGui import *
from pyui.dialogNewItem import Ui_DialogNewItem
from data import ItemData
import os

class DialogNewItem(QDialog, Ui_DialogNewItem):
    def __init__(self, parent, itemData=None):
        QDialog.__init__(self, parent)
        self.setupUi(self)
        self.parent = parent
        if itemData:
            self.lineEditName.setText(itemData.name)
            self.lineEditIn.setText(itemData.inFile)
            self.lineEditOut.setText(itemData.outFile)
        self.prjData = parent.getProjectData()
        self.btnIn.pressed.connect(self.onButtonIn)
        self.btnOut.pressed.connect(self.onButtonOut)
    
    def getItemData(self):
        name = self.lineEditName.text()
        inFile = self.lineEditIn.text()
        outFile = self.lineEditOut.text()
        return ItemData(self.isInputResouce(), name, inFile, outFile)
    
    
    def accept(self):
        if self.lineEditName.text() and self.lineEditIn.text() and self.lineEditOut.text():
            self.done(1)
        else:
            QMessageBox.critical(self, self.tr("Error"), self.tr("You must fill all fields."))
    
    def onButtonIn(self):
        lastIn = self.prjData.getInPath() or self.prjData.getDir() or os.environ['HOME']
        path = QFileDialog.getOpenFileName(self, self.tr("ui file"), lastIn, filter="*.ui *.qrc")[0]
        if path:
            baseName = os.path.basename(str(path))
            name = os.path.splitext(baseName)[0]
            self.lineEditName.setText(name)
            self.lineEditIn.setText(path)
        
    
    def onButtonOut(self):
        if self.lineEditName.text():
            baseName = os.path.basename(self.lineEditIn.text())
            fileName = os.path.splitext(baseName)[0]
            if self.isInputResouce():
                fileName += "_rc"
            
        lastOut = self.prjData.getOutPath() or self.prjData.getDir() or os.environ['HOME']
        lastDir = os.path.join(lastOut, fileName+".py")
        path = QFileDialog.getSaveFileName(self, self.tr("Python file"), lastDir, "*.py", options=QFileDialog.DontConfirmOverwrite)[0]
        if path:
            self.lineEditOut.setText(path)
    
    
    def isInputResouce(self):
        return os.path.splitext(self.lineEditIn.text())[1] == ".qrc"
    
    
    
            
            
            
