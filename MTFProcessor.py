from PyQt5 import Qt, QtCore, QtGui, QtWidgets
from mainwindow import Ui_MainWindow
import pyqtgraph as pg
import pyqtgraph.exporters
import regex, csv, lmfit, scipy, numpy, fnmatch, sys, math
import matplotlib.pyplot as plt
import MTF_Module

def SelectFile(self):

    selectedFiles, _filter = QtWidgets.QFileDialog.getOpenFileNames(ui, 'Select Files', "", "XLSX (*.xlsx)")
    global fileNames
    fileNames = []
    ui.fileList.clear()
    if len(selectedFiles) == 0:
        ShowBox()
    else:
        for i in selectedFiles:
            text = regex.split('/', i)
            fileNames.append(text[-1])
        ui.fileList.addItems(fileNames)
    
def Run(self):
    ui.plotArea.clear()
    ui.plotArea.setXRange(0,10, padding=0)
    ui.plotArea.setYRange(0,1.25, padding=0)
    ui.plotArea.addLegend()
    if ui.fileList.count() == 0:
        ShowBox()
    else:
        ui.progressBar.setMaximum(ui.fileList.count())
        for index, file in enumerate(fileNames):
            #ui.label.setText("Working on file number "+str(index+1)+" of "+str(len(fileNames)))
            #ui.label.repaint()
            ui.progressBar.setValue(index)
            numberOfPixels, pixelPitch, distance, xValues, yValues = MTF_Module.mtfProcessor(file)
            ui.plotArea.plot(xValues, yValues, pen=pg.mkPen(color=pg.intColor(index), width=5), name=str(numberOfPixels)+" pixels with "+str(pixelPitch)+" mm pitch at "+distance+" mm into the light spreader")
        ui.progressBar.setValue(ui.fileList.count())
    #ui.label.setText("Run complete")

def Save(self):
    exporter = pg.exporters.ImageExporter(ui.plotArea.plotItem)
    fileName, _filter = QtWidgets.QFileDialog.getSaveFileName(ui, 'Save Graph', "", "PNG (*.png)")
    exporter.export(fileName)

def QtInfo(self):
    msg = QtWidgets.QMessageBox()
    title = "Qt Information"
    message = "This program was made with Qt version " + QtCore.QT_VERSION_STR + " and PyQt version " + Qt.PYQT_VERSION_STR
    msg.setWindowTitle(title)
    msg.setText(message)
    msg.setIcon(QtWidgets.QMessageBox.Information)
    msg.exec_()

def ProgramInfo(self):
    msg = QtWidgets.QMessageBox()
    title = "Program Information"
    message = "This program reads in xlsx files from ZEMAX and find the Modulation Transfer Function. Data files must be in the same directory as the EXE file, but with the select file button you can select an unlimited number of files and analyze them at once by selecting the Run button. The data will all be plotted on the same graph, normalized to one. Use the Save button to save the graph as a PNG."
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

    ui.selectFileButton.clicked.connect(SelectFile)
    ui.runButton.clicked.connect(Run)
    ui.saveButton.clicked.connect(Save)

    ui.actionSelectFiles.triggered.connect(SelectFile)
    ui.actionQtInfo.triggered.connect(QtInfo)
    ui.actionProgramInfo.triggered.connect(ProgramInfo)

    ui.actionExit.triggered.connect(Exit)

    ui.sys.exit(app.exec_())
