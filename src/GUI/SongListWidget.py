#!/usr/bin/python3
# -*- coding: utf8 -*-



import sys
from PyQt4 import QtGui, QtCore, Qt

class SongListWidget(QtGui.QTableWidget):
    def __init__(self,songNumber = 3,parent = None):
        QtGui.QTableWidget.__init__(self,songNumber,4,parent)
        self.setHorizontalHeaderLabels("Durée;Artiste;Album;Titre".split(";"))
        self.setSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding);
        self.setShowGrid(False)
        self.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.verticalHeader().hide()

        #Stretches the song title space
        songNameHeader = self.horizontalHeader()
        songNameHeader.setStretchLastSection(True)