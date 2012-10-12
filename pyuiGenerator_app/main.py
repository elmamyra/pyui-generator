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
from pyui.mainWindow import Ui_MainWindow
from dialogNewProject import DialogNewProject
from dialogNewItem import DialogNewItem
from dialogAddMulti import DialogAddMulti
from itemWidget import ItemWidget
from data import ProjectData
import sys, os



class Main(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self, parent)
        self.setupUi(self)
        QCoreApplication.setOrganizationName("pyui-generator")
        self.projectData = None
        self.listItemWidget = []
        self.isModified = False
        self.restore()
        self.connectEvent()
        
        
    def connectEvent(self):
        self.actionNew.triggered.connect(self.onNewProject)
        self.actionLoad.triggered.connect(self.onLoadProject)
        self.actionSave.triggered.connect(self.onSaveProject)
        self.actionAddItem.triggered.connect(self.onAddItem)
        self.actionAddMulti.triggered.connect(self.onAddMulti)
        self.actionGenerateAll.triggered.connect(self.onGenerateAll)
        
    
    def restore(self):
        """restore settings"""
        s = QSettings()
        #restore geometry and toolbars state
        self.restoreGeometry(s.value("geometry"))
        self.restoreState(s.value("toolState"))
        
        #load the last project if there
        lastProjectPath = s.value("lastProjectPath")
        if lastProjectPath and os.path.exists(lastProjectPath):
            self.load(lastProjectPath)
        else:
            self.disableTool(True)
            
        if s.value("synchronize") == "true":
            self.actionSync.setChecked(True)
            
    def disableTool(self, val):
        """disabled or enabled tools"""
        toolList = (self.actionSave, self.actionAddItem, self.actionGenerateAll,
                    self.actionAddMulti, self.actionSync)
        for tool in toolList:
            tool.setDisabled(val)
    
    def deleteItem(self, index):
        self.projectData.deleteItem(index)
        self.updateItemWidget()
    
    def getProjectData(self):
        return self.projectData
    
    
    
    
    def onNewProject(self):
        if not self.checkSave():
            return
        
        dlg = DialogNewProject(self)
        if dlg.exec_():
            self.clearLayout()
            self.projectData = ProjectData(dlg.getName(), dlg.getLib())
            self.disableTool(False)
            self.modified()
    
    
    def load(self, path):
        prjData = ProjectData.load(path)
        
        if prjData:
            self.projectData = prjData
            self.clearLayout()
            for itemData in self.projectData.getItems():
                self.addItemWidget(itemData)
            
            self.isModified = False
            self.setTitle()
            
            return True
        
        return False
            
    
    def onLoadProject(self):
        if not self.checkSave():
            return
        if self.projectData and os.path.exists(self.projectData.getPath()):
            dir_ = self.projectData.getPath()
        else:
            dir_ = os.environ['HOME']
        
        path = QFileDialog.getOpenFileName(self, self.tr("Load project"), dir_, "*.uig")[0]
        if path:
            if not self.load(path):
                QMessageBox.critical(self, self.tr("Error"), self.trUtf8("Could not load project."))
            
    
    def saveAs(self):
        dir_ = os.path.join(os.environ['HOME'], self.projectData.getName()+".uig")
        path = QFileDialog.getSaveFileName(self, self.tr("Save project"), dir_, "*.uig")[0]
        if path:
            ext = os.path.splitext(path)[1]
            if ext != ".uig":
                path += ".uig"
            self.projectData.setPath(path)
            self.save()
            
    
    def save(self):
        self.projectData.save()
        self.isModified = False
        self.setTitle()
    
    def onSaveProject(self):
        if not self.projectData:
            return
        
        path = self.projectData.getPath()
        
        if path and os.path.exists(path):
            self.save()
        else:
            self.saveAs()
            
    def onAddItem(self):
        dlg = DialogNewItem(self)
        if dlg.exec_():
            itemData = dlg.getItemData()
            self.addItem(itemData)
            
    def onAddMulti(self):
        dlg = DialogAddMulti(self)
        if dlg.exec_():
            for itemData in dlg.iterData():
                self.addItem(itemData)
            
    def editItem(self, index):     
        itemData = self.projectData.getItemData(index)
        dlg = DialogNewItem(self, itemData)
        if dlg.exec_():
            itemData = dlg.getItemData()
            self.projectData.setItemData(index, itemData)
            self.setInOutPath(itemData)
            self.updateItemWidget()
    
    def addItem(self, itemData):
        for loadedData in self.projectData.getItems():
            if loadedData == itemData:
                if QMessageBox.question(self, self.tr("Already exists"), 
                    self.tr("<b>{0}</b> already exists.<br/>Add still?").format(itemData.name),
                    QMessageBox.Yes | QMessageBox.No) == QMessageBox.No:
                    return
                break
                
        self.projectData.addItemData(itemData)
        self.setInOutPath(itemData)
        self.addItemWidget(itemData)
        self.modified()
       
    
    def setInOutPath(self, itemData):
        self.projectData.setInPath(os.path.split(itemData.inFile)[0])
        self.projectData.setOutPath(os.path.split(itemData.outFile)[0])
           
    def addItemWidget(self, itemData):
        itemIndex = self.layoutItems.count()
        itemWidget = ItemWidget(self, itemData, itemIndex)
        self.layoutItems.addWidget(itemWidget)
        self.listItemWidget.append(itemWidget)
            
    
    def isSynchronizeMode(self):
        return self.actionSync.isChecked()
    
    def moveItem(self, oldId, newId):
        self.projectData.moveItem(oldId, newId)
        self.updateItemWidget()

    
    def updateItemWidget(self):
        self.clearLayout()
        for itemData in self.projectData.getItems():
            self.addItemWidget(itemData)
        self.modified()
    
    def onGenerateAll(self):
        for itemWidget in self.listItemWidget:
            itemWidget.exec_()
            
        self.showMessage(self.tr("Generation of all files ending"))
    
    def modified(self):
        self.isModified = True
        self.setTitle()
    
    def setTitle(self):
        title = "pyui-generator"
        if self.projectData:
            title += " - "+self.projectData.getName()
            
        if self.isModified:
            title += "*"
            
        self.setWindowTitle(title)
    
    def checkSave(self):
        if self.isModified:
            mess = self.tr("The project <b>{0}</b> has been modified.<br/>Save changes?").format(self.projectData.getName())
            val = QMessageBox.warning(self, self.tr("Save changes"), mess, QMessageBox.Cancel | QMessageBox.Yes | QMessageBox.No)
            if val == QMessageBox.Cancel:
                return False
            
            elif val == QMessageBox.Yes:
                self.isModified = False
                self.projectData.save()
                
            self.setTitle()
        return True
                
    
    def showMessage(self, mess, time=2000):
        self.statusBar().showMessage(mess, time)
     
    def clearLayout(self):
        for i in range(self.layoutItems.count()): 
            self.layoutItems.takeAt(0).widget().close()
            
        self.listItemWidget = []
    
                
    def closeEvent(self, evt):
        if not self.checkSave():
            evt.ignore()
            return
        
        s = QSettings()
        s.setValue("geometry", self.saveGeometry())
        s.setValue("toolState", self.saveState())
        s.setValue("synchronize", self.isSynchronizeMode())
        if self.projectData:
            s.setValue("lastProjectPath", self.projectData.getPath())
        
   
def run():        
    app = QApplication(sys.argv)
    locale = QLocale.system().name()
    
    translator=QTranslator ()
    translator.load(os.path.join("i18n", locale))
    app.installTranslator(translator)
    
    
    
    translatorQt=QTranslator ()
    translatorQt.load("qt_" + locale,   
                    QLibraryInfo.location(QLibraryInfo.TranslationsPath))
    
    app.installTranslator(translatorQt)
    
    
    
    main = Main()
    main.show()
    sys.exit(app.exec_())

if __name__=="__main__":
    run()