from scipy import asarray as ar,exp

def gaus(x,a,x0,sigma):
    return a*exp(-(x-x0)**2/(2*sigma**2))

def gaus_parameters(x, y):
    n = len(x)
    mean = sum(x*y)/n
    sigma = sum(y*(x-mean)**2)/n
    p0 = [1, mean, sigma]

    return p0
