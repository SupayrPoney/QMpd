#!/usr/bin/python3
# -*- coding: utf8 -*-



import sys
from PyQt4 import *
from PyQt4.QtCore import QDir


class TreeWidget(QtGui.QTreeView):
    """ """
    def __init__(self,parent = None, path = "/home/"):
        """ """
        QtGui.QTreeView.__init__(self,parent)

        # The model.
        self.model = QtGui.QFileSystemModel()
        # You can setRootPath to any path.
        self.model.setRootPath(path)
        self.setHeaderHidden(True)
        # Set the model of the self.
        self.setModel(self.model)
        # Set the root index of the self as the user's home directory.
        self.setRootIndex(self.model.index(path))

        #Hides size, date etc.
        self.setColumnHidden(1,True)
        self.setColumnHidden(2,True)
        self.setColumnHidden(3,True)


