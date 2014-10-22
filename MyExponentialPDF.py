import numpy as np
import pylab as pl
import matplotlib.pyplot as plt
import math
import numpy.random as rand
import scipy.optimize as opt


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
        return max([self.evaluate(x) for x in [x for x in np.arange(a,b,stepSize)]])
        #return 0

#exponential pdf which extends the PDF class
class ExponentialPDF(PDF):

    def __init__(self,a,b,tau):
        PDF.__init__(self,a,b)
        self.tau=tau
        self.maxVal=self.maxValue(a,b,stepSize)

	#normal exponential
    def evaluate(self, x):
	coef=self.tau**-1
	expon=-x*(self.tau**-1)
        return coef*math.exp(expon)

	#generates a new random number from a exponential distribution
    def next(self):
        fromExponential=False
        while fromExponential==False:
            x1=rand.random()
            x1=self.toRangeAB(self.a,self.b,x1)
            y1=self.evaluate(x1)
            y2=self.toRangeFmax(self.maxVal, rand.random())
            if y2<y1:
                fromExponential=True
                return x1
            else:
                pass

	#numerical integration of exponential pdf using monte carlo method
'''    def integralNumeric(self,numPoints):
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
	return rectArea*f'''

	#returns integral of exponential function between -infinity and infinity
'''    def integralAnalytic(self,b):
	return 1-math.exp(self.tau*b)'''

stepSize = 0.0001
f = open("decay times","w")

def fitFunc(x,t):
    return (1/t)*np.exp(-x/t)

def main():
	#defines range
    a = 0
    b = 15
   
    tau=2.2
    targetValue=1000 #ammount of random numbers generated
    numPoints=11000 #the number of points you need to generate from monte carlo method to be accurate within 1%

    expo=ExponentialPDF(a,b,tau)

    maxVal=expo.maxValue(a,b,stepSize) # maximum of exponential

	#list of points from the exponential distribution
    values=[0 for x in range(0,targetValue)] 
    for i in range(0,targetValue):
        values[i]=expo.next()
        f.write(str(values[i]) + '\n')

    f.close()

	#Maximum Likelihood estimation of tau by taking derivative of log likelihood, setting it to 0 and solving for tau	
    MLEst = (sum(values))/targetValue 
    print MLEst


    hist1, histEdges1 = np.histogram(values, bins=50)
 #   xData = [(histEdges[i]+histEdges[i+1])/2 for i in range(0,len(histEdges)-1)]
 #   yData = [fitFunc(x,2.2) for x in xData]
    popt1, pcov1 = opt.curve_fit(fitFunc,histEdges1[1:len(histEdges1)],hist1)
    print np.exp(popt1)

    hist2, histEdges2 = np.histogram(values, bins=50)
 #   xData = [(histEdges[i]+histEdges[i+1])/2 for i in range(0,len(histEdges)-1)]
 #   yData = [fitFunc(x,2.2) for x in xData]
    popt2, pcov2 = opt.curve_fit(fitFunc,histEdges2[1:len(histEdges2)],hist2)
    print np.exp(popt2)
    #plt.bar(xData,yData)
    #plt.show()

#    plotting histogram
#    plt.hist(values, bins=15)
#    plt.show()


 #   paramEstimates = [0 for x in range(0,1000)]
#    popt = opt.minimize(expo.evaluate,1)
#    print popt
 #   for i in range(0,len(paramEstimates)):
 #       xs = np.linspace(a,b,len(values))
 #       popt, pcov = opt.curve_fit(fitFunc,xs,values)	
 #       paramEstimates[i]=popt
 #   print np.mean(paramEstimates)
 #   plt.hist(paramEstimates, bins = 15)
 #   plt.show
	


#calculating monte carlo accuracy
#    numDels=100#number of times
#    trueIntegral=expo.integralAnalytic(b)
#    dels = [0 for x in range(0,numDels)]
#    sumDels = 0
#    sumSquares =0
#    for i in range(0,numDels):
#        dels[i]=abs(trueIntegral-expo.integralNumeric(numPoints))
#        #print dels[i]
#        sumSquares = sumSquares + (dels[i]**2)
#        sumDels = sumDels + dels[i]
#	
#    std = math.sqrt(sumSquares/(numDels-1))'''



if __name__=='__main__':
    main()
