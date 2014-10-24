import numpy as np
import pylab as pl
import matplotlib.pyplot as plt
import math
import numpy.random as rand
import scipy.optimize as opt
from MyGaussianPDFFinal import *



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


stepSize = 0.0001

def fitFunc(x,t):
    return (1/t)*np.exp(-x/t)

def nll(vals,tau):
	fitF = [0 for x in range(0,len(vals))]
	for i in range(0,len(vals)):
		fitF[i] = fitFunc(vals[i],tau)
		#if fitF[i] < 0.000000001:
		#	fitF[i] = 0.0001
	return -sum([np.log(fitF[x]) for x in range(0,len(fitF))])

def minimize(vals):

	stepSize = 0.1
	improvement = True
	initialTau = 2
	tau=initialTau
	iterations=0
	while improvement:
		if math.fabs(nll(vals, tau+stepSize) - nll(vals,tau)) >30 and iterations <=1000:
			stepSize *=1.2
			tau = tau+stepSize
			iterations+=1
		elif math.fabs(nll(vals, tau+stepSize) - nll(vals,tau)) >5 and iterations <=1000:
				stepSize = 0.1
				tau = tau+stepSize
				iterations+=1
		elif math.fabs(nll(vals, tau+stepSize) - nll(vals,tau)) >0.2 and iterations <=1000:
				stepSize*=0.5
				tau = tau+stepSize
				iterations+=1
		else:
			improvement=False
	return tau
				
def runI():
	#defines range
    a = 0
    b = 15
   
    tau=2.2
    targetValue=1000 #ammount of random numbers generated+


    expo=ExponentialPDF(a,b,tau)

#    maxVal=expo.maxValue(a,b,stepSize) # maximum of exponential

	#list of points from the exponential distribution
    values=[0 for x in range(0,targetValue)] 
    for i in range(0,targetValue):
        values[i]=expo.next()


	#Maximum Likelihood estimation of tau by taking derivative of log likelihood, setting it to 0 and solving for tau	
 #   MLEst = (sum(values))/targetValue 
#    print MLEst

    tauPredicted = minimize(values)
    return tauPredicted
	
def main():
	f = open("decayTimes.txt","w")
	tau = [0 for x in xrange(0,200)]
	for i in range(0,len(tau)):
		tau[i]=runI()
        f.write(str(tau[i]) + '\n')
	print tau
	plt.hist(tau, bins=15)
	plt.show()
	f.close()

#    plotting histogram


if __name__=='__main__':
    main()

