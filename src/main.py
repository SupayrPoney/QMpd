#!/usr/bin/python
# -*- coding: utf8 -*-

import sys
from PyQt4 import QtGui
from GUI import MainWindow


def main():
    """ """  
    app = QtGui.QApplication(sys.argv)
    myapp = MainWindow.MainWindow()
    myapp.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()