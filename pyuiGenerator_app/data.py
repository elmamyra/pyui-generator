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

import cPickle
import os

class ItemData:
    def __init__(self, isResource, name, inFile, outFile):
        self.isResource = isResource
        self.name = name
        self.inFile = inFile
        self.outFile = outFile
    
    def __eq__(self, data):
         
        if isinstance(data, ItemData):
            if self.inFile == data.inFile \
                and self.outFile == data.outFile \
                and self.name == data.name:
                return True
        return False
    
    def __repr__(self):
        return "<ItemData isResource: {0}, name: {1}, inFile: {2}, outFile: {3}"\
                .format(self.isResource, self.name, self.inFile, self.outFile)
        

class ProjectData:
    PYSIDE, PYQT = range(2)
    def __init__(self, name="", lib=PYSIDE):
        self._name = name
        self._lib = lib
        self._items = []
        self._path = ""
        self._inPath = ""
        self._outPath = ""
        
    
        
    def getData(self):
        return self._name, self._lib, self._items, self._path, self._inPath, self._outPath
    
    def setData(self, *data):
        self._name, self._lib, self._items, self._path, self._inPath, self._outPath = data
        
        
    def addItemData(self, itemData):
        self._items.append(itemData)
    
    def moveItem(self, oldId, newId):
        itemData = self._items[oldId]
        self._items[oldId] = None
        self._items.insert(newId, itemData)
        self._items.remove(None)
        
    def deleteItem(self, index):
        self._items.pop(index)
        
   
    def getName(self):
        return self._name
    
    def getLib(self):
        return self._lib
    
    def getItems(self):
        return self._items
    
    def getItemData(self, index):
        return self._items[index]
    
    def getDir(self):
        return os.path.split(self._path)[0]
    
    def getPath(self):
        return self._path
    
    def getInPath(self):
        return self._inPath
    
    def getOutPath(self):
        return self._outPath
    
    def setPath(self, path):
        self._path = path
    
    def setItemData(self, index, itemData):
        self._items[index] = itemData
    
#    def setModified(self, val):
#        self._isModified = val
        
    def setInPath(self, path):
        self._inPath = path
        
    def setOutPath(self, path):
        self._outPath = path
        
#    def isModified(self):
#        return self._isModified
    
    def save(self):
        if self._path:
            try:
                cPickle.dump(self.getData(), open(self._path, "w"))
                return True
            except:
                return False
    
    @staticmethod
    def load(path):
        try:
            data = cPickle.load(open(path))
            prjData = ProjectData()
            prjData.setData(*data)
            prjData.setPath(path)
            return prjData
        except:
            return None
        
