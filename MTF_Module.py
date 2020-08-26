import numpy as np
import xlrd
from scipy import signal
from scipy import interpolate
from scipy import optimize
from scipy import asarray as ar,exp
import regex as re
import matplotlib.pyplot as plt
import Rise_Distance
import Flat_Profile
import Normalize
import Gaus

def mtfProcessor(fileName):

    #Use the file name to get information about the simulation
    text = re.findall(r'\d*\.?\d+', fileName)
    
    
    numberOfRows=int(text[0])
    numberOfPixels=int(text[1])
    pixelPitch=int(text[2])
    lsDistance=text[4]
    xRange = numberOfPixels*pixelPitch

    #Pull in data from the file, sum the y-components, and create the x-values
    rawData = xlrd.open_workbook(fileName)
    dataSheet = rawData.sheet_by_index(0)
    dataArray = []
    for row in range(0, dataSheet.nrows):
        dataArray.append([row.value for row in dataSheet.row(row)])
    summedArray = np.sum(dataArray, axis=0)
    xStepNumber = len(summedArray)
    xStart = -1*xRange/2
    xValues = np.linspace(xStart, -1*xStart, xStepNumber)

    #Find a window that works with the number of x points and use it to smooth the data
    window = int(xStepNumber/numberOfPixels)
    if (window % 2) == 0:
        window+=1
    ySmooth = signal.medfilt(summedArray, window)

    #Find the max value, then use that to find when we hit 10% and 90% of the max
    yMax, yMaxID, linePairConv= Rise_Distance.riseDistance(ySmooth, xValues)

    #Make a flat profile
    yFlat = Flat_Profile.flatProfile(ySmooth, yMaxID, yMax)
    ERF = interpolate.PchipInterpolator(xValues,yFlat)
    yERF = ERF(xValues)

    #Use the flat profile to make the line spread function and normalize it
    sxValues = xValues[:-1]
    LSF = np.diff(yERF)
    nLSF = Normalize.normalize(LSF)

    #Fit the normalized lsf with a gaussian function
    p0=Gaus.gaus_parameters(sxValues, nLSF)
    popt,pcov = optimize.curve_fit(Gaus.gaus,sxValues,nLSF,p0)
    gFit = Gaus.gaus(sxValues, *popt)

    #Take the Fourier transform of the line spread function and use
    #it to find the modulation transfer function
    LSFfft = np.fft.fft(gFit)
    totalMTF = Normalize.normalize(abs(LSFfft/xRange))
    middleIndex = int(len(totalMTF)/2)
    halfMTF = totalMTF[0:middleIndex]
    freqEnd = (len(LSFfft)/2)-1
    freqConv = linePairConv*pixelPitch*2/xRange
    freqDomain = np.linspace(0, freqEnd, middleIndex)
    freqDomain *= freqConv
    return (numberOfPixels, pixelPitch, lsDistance, freqDomain, halfMTF)


