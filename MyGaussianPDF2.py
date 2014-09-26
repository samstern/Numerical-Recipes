import numpy as np
import pylab as pl
import matplotlib.pyplot as plt
import math
import sys
import numpy.random as rand
sys.setrecursionlimit(10000)

class PDF:

    def __init__(self,a,b):
        self.a=a
        self.b=b
   
    @staticmethod   
    def toRangeAB(a,b,x):
        return a+(b-a)*x

    @staticmethod
    def toRangeFmax(fmax,y):
        return fmax*y

    def evaluate(self, x):
        pass

    def maxValue(self,a,b,stepSize):
        #xs= [x for x in np.arange(a,b,stepSize)]
        #y = [self.evaluate(x) for x in [x for x in np.arange(a,b,stepSize)]]
        return max([self.evaluate(x) for x in [x for x in np.arange(a,b,stepSize)]])
        #return 0

class GaussianPDF(PDF):

    def __init__(self,a,b,mu,sigma):
        PDF.__init__(self,a,b)
        self.mu=mu
        self.sigma=sigma

    def evaluate(self, x):
        coef=1/(self.sigma*(math.sqrt(2*math.pi)))
        expon=-((x-self.mu)**2)/(2*self.sigma**2)
        return coef*math.exp(expon)

    def next(self,maxVal):
       
        fromGaussian=False
        while fromGaussian==False:
            x1=rand.random()
            x1=PDF.toRangeAB(self.a,self.b,x1)
            #maxVal=self.maxValue(self.a, self.b, stepSize)
            y1= self.evaluate(x1)
            y2=self.toRangeFmax(maxVal, rand.random())
            if y2<y1:
                fromGaussian=True
                return x1
            else:
                pass

    

stepSize = 0.0001

def main():
   
    a = -5
    b = 5
   
    sigma = 2
    mu=0
    targetValue=10000

    gaus=GaussianPDF(a,b,mu,sigma)

    values=[0 for x in range(0,targetValue)]

    maxVal=gaus.maxValue(a,b,stepSize)

    for i in range(0,targetValue):
        values[i]=gaus.next(maxVal)
        print values[i]

    plt.hist(values, bins=15)
    plt.show()

if __name__=='__main__':
    main()
