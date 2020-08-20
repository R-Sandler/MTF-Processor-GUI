from PyQt5 import QtCore, QtGui, QtWidgets
import pyqtgraph as pg

class Ui_MainWindow(QtWidgets.QWidget):
    import sys
    def __init__(self, parent=None):
        super(Ui_MainWindow, self).__init__(parent)
        self.setupUi(self)
        
    def setupUi(self, MainWindow):
        #This is all just drawing the GUI and setting things in place
        MainWindow.setObjectName("MTF Processor")
        MainWindow.resize(1500, 1100)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 1500, 41))
        self.menuBar.setObjectName("menuBar")
        fileMenu = self.menuBar.addMenu('&File')
        infoMenu = self.menuBar.addMenu('&Info')
        pg.setConfigOption('background', 'w')
        pg.setConfigOption('foreground', 'k')
        self.actionSelectFiles = fileMenu.addAction("Select Files")
        self.actionExit = fileMenu.addAction("Exit")
        self.actionQtInfo = infoMenu.addAction("About Qt")
        self.selectFileButton = QtWidgets.QPushButton(self.centralWidget)
        self.selectFileButton.setGeometry(20, 61, 180, 60)
        self.selectFileButton.setDefault(False)
        self.selectFileButton.setFlat(False)
        self.selectFileButton.setObjectName("selectFileButton")
        self.selectFileButton.setText("Select File(s)")
        self.runButton = QtWidgets.QPushButton(self.centralWidget)
        self.runButton.setGeometry(750, 61, 80, 60)
        self.runButton.setDefault(False)
        self.runButton.setFlat(False)
        self.runButton.setObjectName("runButton")
        self.runButton.setText("Run")
        self.saveButton = QtWidgets.QPushButton(self.centralWidget)
        self.saveButton.setGeometry(1370, 61, 80, 60)
        self.saveButton.setDefault(False)
        self.saveButton.setFlat(False)
        self.saveButton.setObjectName("saveButton")
        self.saveButton.setText("Save")
        self.plotArea = pg.PlotWidget(self.centralWidget)
        self.plotArea.setObjectName("plotArea")
        self.plotArea.setGeometry(QtCore.QRect(750, 141, 700, 800))
        self.fileList = QtWidgets.QListView(self.centralWidget)
        self.fileList.setGeometry(20, 141, 500, 800)
        self.fileList.setObjectName("fileList")

        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.retranslateUi(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MTF Processor"))
