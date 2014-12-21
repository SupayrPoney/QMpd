#!/usr/bin/python2
# -*- coding: utf8 -*-

import sys
import os

from PyQt4 import QtGui, QtCore, Qt
from PyQt4.QtCore import QDir

import TreeWidget, ButtonsWidget



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


    def initArborescence(self,path = QDir.rootPath()):

        horizontalSplitter = QtGui.QSplitter()
        # The model.
        model = QtGui.QFileSystemModel()
        # You can setRootPath to any path.
        model.setRootPath(path)
        # List of views.
        views = []
        # Create the view in the splitter.
        view = QtGui.QTreeView()
        view.setHeaderHidden(True)
        # Set the model of the view.
        view.setModel(model)
        # Set the root index of the view as the user's home directory.
        view.setRootIndex(model.index(path))

        view.setColumnHidden(1,True)
        view.setColumnHidden(2,True)
        view.setColumnHidden(3,True)

        button = QtGui.QPushButton("Coucou")
        button2 = QtGui.QPushButton("Allo")

        horizontalSplitter.addWidget(view)
        horizontalSplitter.addWidget(button)

        verticalSplitter = QtGui.QSplitter()
        verticalSplitter.setOrientation(QtCore.Qt.Vertical)
        verticalSplitter.addWidget(horizontalSplitter)
        verticalSplitter.addWidget(button2)

        self.mainLayout.addWidget(verticalSplitter,0,0)

        self.mainWidget.setLayout(self.mainLayout)

    def previous(self):
        pass

    def next(self):
        pass

    def play(self):
        pass


        
        
