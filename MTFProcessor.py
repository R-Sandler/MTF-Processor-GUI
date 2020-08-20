from PyQt5 import Qt, QtCore, QtGui, QtWidgets
from mainwindow import Ui_MainWindow
import pyqtgraph as pg
import regex, csv, lmfit, pandas, scipy, numpy, fnmatch, sys, math
import matplotlib.pyplot as plt
import MTF_Module

def SelectFile(self):

    selectedFiles, _filter = QtWidgets.QFileDialog.getOpenFileNames(ui, 'Select Files', "", "XLSX (*.xlsx)")

    if len(selectedFiles) == 0:
        ShowBox()
    else:
        model = QtGui.QStandardItemModel()
        ui.fileList.setModel(model)
        #fileNames = []
        for i in selectedFiles:
            text = regex.split('/', i)
            fileNames.append(text[-1])
            item = QtGui.QStandardItem(text[-1])
            model.appendRow(item)
        #print(fileNames)
    
def Run(self):
    #print(fileNames)
    ui.plotArea.setXRange(0,10, padding=0)
    ui.plotArea.setYRange(0,1.25, padding=0)
    ui.plotArea.addLegend()
    if len(fileNames) == 0:
        ShowBox()
    else:
        for index, file in enumerate(fileNames):
            #print("Working on file number "+str(index+1))
            numberOfPixels, pixelPitch, distance, xValues, yValues = MTF_Module.mtfProcessor(file)
            ui.plotArea.plot(xValues, yValues, pen=pg.mkPen(color=pg.intColor(index), width=5), name=str(numberOfPixels)+" pixels with "+str(pixelPitch)+" mm pitch at "+distance+" mm into the light spreader")


def QtInfo(self):
    msg = QtWidgets.QMessageBox()
    title = "Qt Information"
    message = "This program was made with Qt version " + QtCore.QT_VERSION_STR + " and PyQt version " + Qt.PYQT_VERSION_STR
    msg.setWindowTitle(title)
    msg.setText(message)
    msg.setIcon(QtWidgets.QMessageBox.Information)
    msg.exec_()

def Exit(self):
    sys.exit(app.exec_())

def ShowBox():
    #The error mesage for missing files
    msg = QtWidgets.QMessageBox()
    title = "Missing files"
    message = "No files are selected. Please select a file."
    msg.setWindowTitle(title)
    msg.setText(message)
    msg.setIcon(QtWidgets.QMessageBox.Warning)
    msg.exec_()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QWidget()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    global fileNames
    fileNames = []

    ui.selectFileButton.clicked.connect(SelectFile)
    ui.runButton.clicked.connect(Run)

    ui.actionSelectFiles.triggered.connect(SelectFile)
    ui.actionQtInfo.triggered.connect(QtInfo)

    ui.actionExit.triggered.connect(Exit)

    ui.sys.exit(app.exec_())
