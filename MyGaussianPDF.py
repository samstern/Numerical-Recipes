import numpy as np
import pylab as pl
import matplotlib.pyplot as plt 
import math
import sys
import numpy.random as rand 
sys.setrecursionlimit(10000)

# finds gaussian f(x) for a given sigma and mu
def gaussianFx(x, sigma, mu):
	coef=1/(sigma*(math.sqrt(2*math.pi)))
	expon=-((x-mu)**2)/(2*sigma**2)
	return coef*math.exp(expon)

#returns the maximum value of f(x) for some function (here the gaussian has been hard coded
#but could be any function). the step size defines the granularity.
def maxValue(a, b, sigma, mu, stepSize):
	xs= [x for x in np.arange(a,b,stepSize)]
	y = [gaussianFx(x, sigma, mu) for x in xs]
	return max(y)

#converts a random number x in the rance 0 to 1 to a randum number between a and b
def toRangeAB(a,b,x):
		return a+(b-a)*x

#converts a random number y to a random number between 0 and fmax
def toRangeFmax(fmax,y):
		return fmax*y

#recursively implemented steps 4-10
def findValues(targetValue, a, b, maxVal, count, sigma, mu):
	x1=rand.random()
	x1=toRangeAB(a,b,x1)
	y1= gaussianFx(x1, sigma, mu)
	y2=toRangeFmax(maxVal, rand.random())
	

	if y2<   y1:
		if count<targetValue:
			randNums[count]=x1
			count+=1
			findValues(targetValue, a, b, maxVal, count, sigma, mu)
		else:
			return randNums
	else:
		pass
		findValues(targetValue, a, b, maxVal, count, sigma, mu)
	return randNums


targetValue=2000
randNums = [0 for x in range(0,targetValue)]


def main():
	a = -5
	b = 5
	stepSize = 0.0001
	sigma = 2
	mu=0
	count=0
	maxVal= maxValue(a, b, sigma, mu, stepSize)

	values = findValues(targetValue, a, b, maxVal, count, sigma, mu)
	print values
	histogram= np.histogram(values,10)
	plt.hist(values, bins=15)
	plt.show()


main()