import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

def fitFunc(x,t):
    return (1/t)*np.exp(-x/t)



xs = np.linspace(0,15,1000)
temp = fitFunc(xs,2.2)

fitParams,fitCovs = curve_fit(fitFunc,xs,temp)
print fitParams
