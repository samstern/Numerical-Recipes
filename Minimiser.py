from Chisq import *

class Minimiser:

	def __init__(self):
		self.setParams()

	def setParams(self, params = [0,0,0,10**6,0.001,False,0,10**3,10**6]):
		self.paramNum
		self.currentParams
		self.currentIteration
		self.maxIterations
		self.convLimit
		self.isFinished
		self.currentCycle
		self.minCycles
		self.previousChisq

        self.__parameters         = matrix([])
        self.__increments         = matrix([])

		

	def set_StartParams(self, params, incs):
        # Expect params to be a (n,1) matrix (column vector)                                                                 
        self.paramNum           = params.shape[0]
        self.parameters         = params
        self.increments         = incs

    def print_StartParams(self):
        print self.parameters
        print self.increments
        print self.paramNum

    def set_ConvLimit(self, conv):
        self.convLimit          = conv

    def set_MaxIterations(self, maxIter):
        self.maxIterations      = maxIter

    def get_isFinished(self):
        return self.__isFinished

	def minimise(self, chisq):
		self.currentIteration +=1
	
		if self.currentIteration > self.maxIterations:
			self.isFinished=True
			print "finished without convergence"
			return self.parameters

		if self.previousChisq<
		
		

def main():
	
	m=1
	c=0
	parameters = [m,c]

	deltaM=0.1
	deltaC=0.1
	stepSizes=[deltaM,deltaC]

	function=Linear()
	minim = Minimiser()
	
	while minim.isFinished() != True:
		function.set_elements([m,c])
		newchisq = function.evaluate()
		params=minim.minimise(newChisq)
