import numpy as np
import pylab as pl
import matplotlib.pyplot as plt
import math
import sys
import numpy.random as rand
sys.setrecursionlimit(10000)

#abstract pdf class
class PDF:

    def __init__(self,a,b):
        self.a=a
        self.b=b
	
	#normalises x to lie between a and b
    @staticmethod   
    def toRangeAB(a,b,x):
        return a+(b-a)*x

	#normalises y to lie between 0 and fmax
    @staticmethod
    def toRangeFmax(fmax,y):
        return fmax*y

	#compute y=f(x) for some probability distribution
    def evaluate(self, x):
        pass

	#naively finds the maximum of a function between a and b
    def maxValue(self,a,b,stepSize):
        #xs= [x for x in np.arange(a,b,stepSize)]
        #y = [self.evaluate(x) for x in [x for x in np.arange(a,b,stepSize)]]
        return max([self.evaluate(x) for x in [x for x in np.arange(a,b,stepSize)]])
        #return 0

#gaussian pdf which extends the PDF class
class GaussianPDF(PDF):

    def __init__(self,a,b,mu,sigma):
        PDF.__init__(self,a,b)
        self.mu=mu
        self.sigma=sigma
        self.maxVal=self.maxValue(a,b,stepSize)

	#normal gaussian
    def evaluate(self, x):
	coef=1/(self.sigma*(math.sqrt(2*math.pi)))
	expon=-((x-self.mu)**2)/(2*self.sigma**2)
        return coef*math.exp(expon)

	#generates a new random number from a gaussian distribution
    def next(self):
        fromGaussian=False
        while fromGaussian==False:
            x1=rand.random()
            x1=self.toRangeAB(self.a,self.b,x1)
            y1= self.evaluate(x1)
            y2=self.toRangeFmax(self.maxVal, rand.random())
            if y2<y1:
                fromGaussian=True
                return x1
            else:
                pass

	#numerical integration of gaussian pdf using monte carlo method
    def integralNumeric(self,numPoints):
	rectArea=self.maxVal*(self.b-self.a)
	counter=0

	for i in range(0,numPoints):
		x=self.toRangeAB(self.a,self.b,rand.random())
		y=self.toRangeFmax(self.maxVal,rand.random())
		if y<self.evaluate(x):
			counter=counter+1
		else:
			pass
	f=float(counter)/float(numPoints)
	return rectArea*f

	#returns integral of gaussian function between -infinity and infinity
    def integralAnalytic(self):
	coef=1/(self.sigma*(math.sqrt(2*math.pi)))
	return coef*self.sigma*math.sqrt(2*math.pi)

stepSize = 0.0001

def main():
	#defines range
    a = -15
    b = 15
   
    sigma = 5
    mu=0
    targetValue=10000 #ammount of random numbers generated
    numPoints=11000 #the number of points you need to generate from monte carlo method to be accurate within 1%

    gaus=GaussianPDF(a,b,mu,sigma)

    maxVal=gaus.maxValue(a,b,stepSize) # maximum of gaussian

	#list of points from the gaussian distribution
    values=[0 for x in range(0,targetValue)] 
    for i in range(0,targetValue):
        values[i]=gaus.next()
	

	#calculating monte carlo accuracy
    numDels=100#number of times
    trueIntegral=gaus.integralAnalytic()
    dels = [0 for x in range(0,numDels)]
    sumDels = 0
    sumSquares =0
    for i in range(0,numDels):
        dels[i]=abs(trueIntegral-gaus.integralNumeric(numPoints))
        #print dels[i]
        sumSquares = sumSquares + (dels[i]**2)
        sumDels = sumDels + dels[i]
	
    std = math.sqrt(sumSquares/(numDels-1))

    print ('std: '+ repr(std))
 

#plotting histogram
    plt.hist(values, bins=15)
    plt.show()
	

if __name__=='__main__':
    main()
