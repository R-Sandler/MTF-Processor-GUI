def riseDistance(ySmooth, xValues):
    #Find the max value, then use that to find when we hit 10% and 90% of the max
    yMax = max(ySmooth)
    yMax10 = next(x for x, val in enumerate(ySmooth) if val > (yMax*0.1))
    yMax90 = next(x for x, val in enumerate(ySmooth) if val > (yMax*0.9))
    yMaxID = next(x for x, val in enumerate(ySmooth) if val == yMax)
    xMax10 = xValues[yMax10]
    xMax90 = xValues[yMax90]
    riseDistance = xMax90-xMax10
    linePairConv = 1/riseDistance
    return (yMax, yMaxID, linePairConv)
