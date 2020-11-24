import numpy as np
import pandas as pd
import scipy as sp
from scipy import signal
from scipy import interpolate
from scipy import optimize
from scipy import asarray as ar,exp
import pyparsing
import matplotlib.pyplot as plt
import MTF_Module
import Rise_Distance
import Flat_Profile
import Normalize
import Gaus
import Make_Plot

for index, file in enumerate(fileNames):
    rint("Working on file number "+str(index+1))
    numberOfPixels, pixelPitch, distance, xValues, yValues = MTF_Module.mtfProcessor(file)
    plt.plot(xValues, yValues, label=str(numberOfPixels)+" pixels with "+str(pixelPitch)+" mm pitch at "+distance+" mm into the light spreader")
plt.legend()
plt.show()
