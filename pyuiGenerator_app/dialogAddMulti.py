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
from pyui.dialogAddMulti import Ui_DialogAddMulti
from data import ItemData
import os

class DialogAddMulti(QDialog, Ui_DialogAddMulti):
    def __init__(self, parent):
        QDialog.__init__(self, parent)
        self.setupUi(self)
        self.parent = parent
        self.listInFile = []
        self.prjData = self.parent.getProjectData()
        self.lineEditOutDir.setText(self.prjData.getOutPath())
        
        self.btnInFile.pressed.connect(self.onInFile)
        self.btnOutDir.pressed.connect(self.onOutDir)
        
    def onInFile(self):
        lastIn = self.prjData.getInPath() or self.prjData.getDir() or os.environ['HOME']
        self.listInFile = QFileDialog.getOpenFileNames(self, self.tr("ui files"), lastIn, filter="*.ui *.qrc")[0]
        text = ", ".join(map(os.path.basename, self.listInFile))
        self.lineEditInFile.setText(text)

    def onOutDir(self):
        lastOut = self.prjData.getOutPath() or self.prjData.getDir() or os.environ['HOME']
        dir_ = QFileDialog.getExistingDirectory(self, self.tr("Python folder"), lastOut)
        self.lineEditOutDir.setText(dir_)
    
    def accept(self):
        if not self.listInFile:
            QMessageBox.critical(self, self.tr("Error"), self.tr("You must select files."))
        elif not os.path.isdir(self.lineEditOutDir.text()):
            QMessageBox.critical(self, self.tr("Error"), self.tr("The folder address is not valid."))
        else:
            self.done(1)
    
      
    def isInputResouce(self):
        return os.path.splitext(self.lineEditIn.text())[1] == ".qrc"
    
    def iterData(self):
        outDir = self.lineEditOutDir.text()
        for inFile in self.listInFile:
            baseName = os.path.basename(inFile)
            name, ext = os.path.splitext(baseName)
            outFileName = name
            isInputResource = False
            if ext == ".qrc":
                outFileName += "_rc"
                isInputResource = True
            outFileName += ".py"
            outFile = os.path.join(outDir, outFileName)
            yield ItemData(isInputResource, name, inFile, outFile)
            
    
            
            