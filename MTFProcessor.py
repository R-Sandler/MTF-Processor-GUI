from PyQt5 import QtCore, QtGui, QtWidgets
from mainwindow import Ui_MainWindow
import pyqtgraph as pg
import re, csv, lmfit, matplotlib, pandas, scipy, numpy, fnmatch, sys, math

def Exit(self):
    sys.exit(app.exec_())

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QWidget()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()

    ui.actionExit.triggered.connect(Exit)

    ui.sys.exit(app.exec_())
