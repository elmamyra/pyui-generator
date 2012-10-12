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
from pyui.dialogNewProject import Ui_DialogNewProject
from data import ProjectData

class DialogNewProject(QDialog, Ui_DialogNewProject):
    def __init__(self, parent):
        QDialog.__init__(self, parent)
        self.setupUi(self)
        self.btnGroup = QButtonGroup(self)
        self.btnGroup.addButton(self.radioButtonPyside, ProjectData.PYSIDE)
        self.btnGroup.addButton(self.radioButtonPyqt, ProjectData.PYQT)
        
    def accept(self):
        if self.lineEditName.text():
            self.done(1)
        else:
            QMessageBox.critical(self, self.tr("Error"), self.tr("You must enter the new project name."))
            
    def getName(self):
        return self.lineEditName.text()
    
    def getLib(self):
        return self.btnGroup.checkedId()
        