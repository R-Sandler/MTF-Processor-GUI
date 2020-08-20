def flatProfile(ySmooth, yMaxID, yMax):
    yFlat = ySmooth
    for x, val in enumerate(yFlat):
        if (x > yMaxID):
            yFlat[x]=yMax
    return yFlat
