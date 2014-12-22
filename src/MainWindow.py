#!/usr/bin/python2
# -*- coding: utf8 -*-

import sys
import os

from PyQt4 import QtGui, QtCore, Qt
from PyQt4.QtCore import QDir

import TreeWidget, SongListWidget#, ButtonsWidget


class MainWindow(QtGui.QMainWindow):
    """ This class is the GUI's main class """
    def __init__(self):
        """Constructor of the class MainWindow"""
        super(MainWindow, self).__init__()
        # init the GUI
        self.initUI()
        
    def initUI(self): 
        """ This methode will initiate the GUI :
        - The Menu bar
        - The toorls bar
        - The main SplitPane
        - The statusBar  
        """             
        # Windows title
        self.setWindowTitle("QMpd")
        self.mainWidget = QtGui.QWidget()
        self.setCentralWidget(self.mainWidget)

        self._statusBar = self.statusBar()
        self._statusBar.showMessage('QMPD v0.0.1')#TODO set current song

        self.mainLayout = QtGui.QGridLayout()

        self.initMenu()

        self.initArborescence()

        #self.initButtons()
   
        self.showMaximized()

    def displayHelp(self):
        """ """
        QtGui.QMessageBox.information(self, "Help", "MPD Client with Qt")

    def displayAbout(self):
        """ Display some info"""
        QtGui.QMessageBox.information(self, "About", "")

    def initMenu(self):
        """ This method will initate the menu """
        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&Fichier')
        helpMenu = menubar.addMenu("&Aide")

        exitAction = QtGui.QAction( 'Quitter', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit application')
        exitAction.triggered.connect(self.close)
        fileMenu.addAction(exitAction)

        aboutAction = QtGui.QAction( "Aide", self)
        aboutAction.setStatusTip("Help")
        aboutAction.triggered.connect(self.displayHelp)
        helpMenu.addAction(aboutAction)

        aboutAction = QtGui.QAction("A propos", self)
        aboutAction.setStatusTip("About")
        aboutAction.triggered.connect(self.displayAbout)
        helpMenu.addAction(aboutAction)

    def initButtons(self):
        self.buttons = ButtonsWidget.ButtonsWidget(self)
        #self.mainLayout.addWidget(self.buttons,0,0)


    def initArborescence(self,path = QDir.rootPath(),songsNumber = 3):

        self.horizontalSplitter = QtGui.QSplitter()

        # List of views.
        views = []
        # Create the view in the splitter.
        view = TreeWidget.TreeWidget(self)

        songsDisplayerLayout = QtGui.QGridLayout()
        songsDisplayerWidget = QtGui.QWidget()

        # Upleft widget. Shows the songs in a directory
        songsDisplayer = SongListWidget.SongListWidget(songsNumber) 

        #Bottom widget, displays the current playlist
        currentPlaylistDisplayer = SongListWidget.SongListWidget(songsNumber) 

        songsDisplayerLayout.addWidget(songsDisplayer,0,0)
        songsDisplayerWidget.setLayout(songsDisplayerLayout)

        self.horizontalSplitter.addWidget(view)
        self.horizontalSplitter.addWidget(songsDisplayerWidget)

        self.horizontalSplitter.setSizes([self.mainWidget.geometry().width()/8,7*self.mainWidget.geometry().width()/8])

        self.verticalSplitter = QtGui.QSplitter()
        self.verticalSplitter.setOrientation(QtCore.Qt.Vertical)
        self.verticalSplitter.addWidget(self.horizontalSplitter)
        self.verticalSplitter.addWidget(currentPlaylistDisplayer)

        self.mainLayout.addWidget(self.verticalSplitter,0,0)

        self.mainWidget.setLayout(self.mainLayout)

    def setCurrentFolderSongs(self):
        pass

    def previous(self):
        pass

    def next(self):
        pass

    def play(self):
        pass


        
        
