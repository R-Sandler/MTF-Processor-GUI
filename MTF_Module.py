import numpy as np
import pandas as pd
import scipy as sp
from scipy import signal
from scipy import interpolate
from scipy import optimize
from scipy import asarray as ar,exp
#import regex as re
from pyparsing import Word, Combine, alphas, nums
import matplotlib.pyplot as plt
import Rise_Distance
import Flat_Profile
import Normalize
import Gaus
import Make_Plot

def mtfProcessor(fileName):
    #fileName = "mtf_1x12pix_6x6mm_0.5mm.xlsx"

    #Use the file name to get information about the simulation
    #text = re.findall(r'\d+', fileName)
    try:
        parseSetup = Word(alphas) + "_" + Word(nums) + "x" + Word(nums) + "pix_" +Word(nums) + "x" +Word(nums) + "mm_" + Combine(Word(nums) + '.' + Word(nums)) +"mm.xlsx"        
        text = parseSetup.parseString(fileName)
    except:
        parseSetup = Word(alphas) + "_" + Word(nums) + "x" + Word(nums) + "pix_" +Word(nums) + "x" +Word(nums) + "mm_" +Word(nums) +"mm.xlsx"
        text = parseSetup.parseString(fileName)
    
    
#    numberOfRows=int(text[0])
#    numberOfPixels=int(text[1])
#    pixelPitch=int(text[2])
#    lsDistance=text[4]
    numberOfRows=int(text[2])
    numberOfPixels=int(text[4])
    pixelPitch=int(text[6])
    lsDistance=text[10]
    xRange = numberOfPixels*pixelPitch

    #Pull in data from the file, sum the y-components, and create the x-values
    dataArray = pd.read_excel(fileName, sheet_name='Sheet1')
    dataArray = np.asarray(dataArray)
    summedArray = np.sum(dataArray, axis=0)
    xStepNumber = len(summedArray)
    xStart = -1*xRange/2
    xValues = np.linspace(xStart, -1*xStart, xStepNumber)

    #Find a window that works with the number of x points and use it to smooth the data
    window = int(xStepNumber/numberOfPixels)
    if (window % 2) == 0:
        window+=1
    ySmooth = signal.medfilt(summedArray, window)

    #Plot the original data and the smoothed data
    #yList = [summedArray, ySmooth]
    #labelList = ['Original Data', 'Smoothed Data']
    #Make_Plot.make_plot(xValues, yList, labelList)

    #Find the max value, then use that to find when we hit 10% and 90% of the max
    yMax, yMaxID, linePairConv= Rise_Distance.riseDistance(ySmooth, xValues)

    #Make a flat profile
    yFlat = Flat_Profile.flatProfile(ySmooth, yMaxID, yMax)
    ERF = interpolate.PchipInterpolator(xValues,yFlat)
    yERF = ERF(xValues)

    #yList = [summedArray, yFlat, yERF]
    #labelList = ['Original Data', 'Flat Data', 'ERF']
    #Make_Plot.make_plot(xValues, yList, labelList)

    #Use the flat profile to make the line spread function and normalize it
    sxValues = xValues[:-1]
    LSF = np.diff(yERF)
    nLSF = Normalize.normalize(LSF)
    #plt.plot(sxValues, nLSF)
    #plt.show()

    #Fit the normalized lsf with a gaussian function
    p0=Gaus.gaus_parameters(sxValues, nLSF)
    popt,pcov = optimize.curve_fit(Gaus.gaus,sxValues,nLSF,p0)
    gFit = Gaus.gaus(sxValues, *popt)
    #yList = [nLSF, gFit]
    #labelList = ['Data', 'Gaussian Fit']
    #Make_Plot.make_plot(sxValues, yList, labelList)

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
    #plt.plot(freqDomain, halfMTF)
    #plt.show()
    return (numberOfPixels, pixelPitch, lsDistance, freqDomain, halfMTF)


