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
from pyui.itemWidget import Ui_ItemWidget
import os
from data import ProjectData
import subprocess
import md5



class ItemWidget(QWidget, Ui_ItemWidget):
    def __init__(self, parent, itemData, index):
        QWidget.__init__(self, parent)
        self.parent = parent
        self.index = index
        self.setupUi(self)
        self.itemData = itemData
        self._hasError = self.checkError()
        self.labelPalette = QPalette(self.labelNom.palette())
        self.isModified = False
        self.setName()
        self.md5Hex = self.getFileMd5()
        
        self.setAcceptDrops(True)
        self.btnExec.pressed.connect(self.exec_)
        self.startTimer(300)
        
        
    def getFileMd5(self):
        if self._hasError:
            return ""
        
        with open(self.itemData.inFile) as f:
            return md5.md5(f.read()).hexdigest()
        
    def checkError(self):
        if not os.path.exists(self.itemData.inFile):
            return True
        
        return False
        
            
#    def hasError(self):      
#        return self._hasError
    
    def timerEvent(self, evt):
        currentHasError = self._hasError
        self._hasError = self.checkError()
        if currentHasError != self._hasError:
            self.md5Hex = self.getFileMd5()
            self.setName()
        
        if self._hasError:
            return
        
        if not self.isModified:
            if self.md5Hex != self.getFileMd5():
                if self.parent.isSynchronizeMode():
                    self.exec_()
                    self.parent.showMessage(self.tr('File "{0}" has been generated automatically')
                                            .format(self.itemData.name))
                else:
                    self.isModified = True
                    self.setName()
                
        
    def setName(self):
        name = self.itemData.name
        if self._hasError:
            pal = self.labelNom.palette()
            pal.setColor(QPalette.Foreground, Qt.red)
            self.labelNom.setPalette(pal)
            self.setToolTip(self.tr("The input file adress is invalid"))
        else:
            self.setToolTip("")
            self.labelNom.setPalette(self.labelPalette)
            if self.isModified:
                name = "<b>{0}</b>".format(name)
        self.labelNom.setText(name)
    
    
    def contextMenuEvent(self, event):
        menu = QMenu()
        actEdit = menu.addAction(QIcon(":/icon/edit"), self.trUtf8("Edit"))
        actDelete = menu.addAction(QIcon(":/icon/delete"), self.trUtf8("Remove"))
        
        action = menu.exec_(event.globalPos())
        if action == actEdit:
            self.parent.editItem(self.index)
        elif action == actDelete:
            self.parent.deleteItem(self.index)
            
       
        
    
    def mousePressEvent(self, e):
        if e.button() == Qt.LeftButton:
            drag = QDrag(self)
            mimeData = QMimeData()
            mimeData.setText(str(self.index))
            drag.setMimeData(mimeData)
            
#            drag.setHotSpot(e.pos() - self.rect().topLeft())
            drag.start(Qt.MoveAction)
        
    
#
    def dragMoveEvent(self, evt):
        if int(evt.mimeData().text()) == self.index:
            evt.ignore()
        else:
            size = 20
            middle = self.geometry().height() / 2
            
            if evt.pos().y() > middle:
                self.layout().setContentsMargins(0, 0, 0, size)
            else:
                self.layout().setContentsMargins(0, size, 0, 0)
            
                
    def dragLeaveEvent(self, evt):
        self.layout().setContentsMargins(0, 0, 0, 0)

    
    def dragEnterEvent(self, e):
        e.accept()

    def dropEvent(self, e):
        self.layout().setContentsMargins(0, 0, 0, 0)
        dropIndex = int(e.mimeData().text())
        
        middle = self.geometry().height() / 2
        index = self.index
        if e.pos().y() > middle:
            index += 1

        self.parent.moveItem(dropIndex, index)
            
        e.accept()
        
    
    def exec_(self):
        
        inFile = self.itemData.inFile
        outFile = self.itemData.outFile
        lib = self.parent.getProjectData().getLib()
        if self.itemData.isResource:
            if lib == ProjectData.PYQT:
                comm = "pyrcc4"
            else:
                comm = "pyside-rcc"
        else:
            if lib == ProjectData.PYQT:
                comm = "pyuic4"
            else:
                comm = "pyside-uic"
        commLine = ("{0} -o {1} {2}").format(comm, outFile, inFile)
        process = subprocess.Popen(commLine, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        err = process.communicate()[1]

        
        if err:
            QMessageBox.warning(self, self.tr("Error"), unicode(err))
        else:
            self.md5Hex = self.getFileMd5()
            self.isModified = False
            self.setName()
            
            
            
            
            
