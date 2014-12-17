#!/usr/bin/python2
# -*- coding: utf8 -*-

import sys
import os

from PyQt4 import QtGui, QtCore



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

        self._statusBar = self.statusBar()
        self._statusBar.showMessage('Welcome!')#TODO set current song

        self.initMenu()

        self.initToolBar()
   
        self.showMaximized()

    def displayHelp(self):
        """ """
        QtGui.QMessageBox.information(self, "Help", "MPD Client")

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


    def initToolBar(self):
        """ This method will initate the toolsBar"""

        previousAction = QtGui.QAction( "Previous", self)
        #reloadAction.setShortcut("Ctrl+R")
        previousAction.setStatusTip("Previous")
        previousAction.triggered.connect(self.previous)
        toolbar.addAction(previousAction)

        pauseAction = QtGui.QAction( "Play", self)
        pauseAction.setShortcut("Ctrl+P")
        pauseAction.setStatusTip("Play/Pause")
        pauseAction.triggered.connect(self.play)
        toolbar.addAction(pauseAction)

        nextAction = QtGui.QAction( "Next", self)
        #reloadAction.setShortcut("Ctrl+R")
        nextAction.setStatusTip("Next")
        nextAction.triggered.connect(self.next)
        toolbar.addAction(nextAction)

    def previous(self):
        pass

    def next(self):
        pass

    def play(self):
        pass


        
        
