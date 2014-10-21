from numpy import matrix
import numpy as np

class Linear:


	def __init__(self,i = matrix[0.,1.]):
		self.m=i[0,0]
		self.c=i[1,0]

	# parameters is a 2x1 matrix where (1,1) is m and (2,1) is c. Note that its actually 0 indexed (so its a 1x0 list of lists)
	def setElements(self, parameters):
		if parameters.shape != (2,1):
			print "Invalid column vector, must be a (2,1) matrix."
		else:
			m=float(parameters[0,0])
			c=float(parameters[0,0])


	def evaluate(self, x):
		return self.m*x+self.c

   # Here we vectorize a function.  Having defined a function eval which acts on a scalar
    # (i.e number) and returns a scalar, vecfn = vectorize(eval) gives us a function vecfn which 
    # will act on np.arrays or matrices and returns a np.array or matrix in which "out_array[i]"
    # is "eval(in_array[i])" **(pseudocode)**.

	def vectorEvaluate(self, j):
		vecfn = np.vectorize(self.evaluate)
		return vecfn

class ChiSq:
	
	    'Class to provide a method to calculate chisq'

    # This is the constructor which sets up the vectors (data x and y) and matrices (inverse error matrix)    
	
	def __init__(self,xin=matrix([]).T, yin = matrix([]).T, ein=matrix([]).T):
		self.xdata  = xin
        self.ydata  = yin
        self.edata  = ein
        self.linear = Linear() 

 # Do some checks                                                                                                   
        if(xin.shape == yin.shape == ein.shape and xin.shape[1] == 1 and xin.shape[0] != 0):
            # This bit constructs the error matrix and takes its inverse                                           
            self.cov    = matrix(np.diag(np.diag(self.edata*self.edata.T)))
            self.Icov   = self.cov.I

            ## Notes ##                                                                                                         
            # The numpy matrix class, with instance A, has methods to transpose: A.T, and inverse: A.I                     
            # self.edata*self.edata.T is a matrix, np.diag(self.edata*self.edata.T) returns a vector of the                
            # diagonal elements of this matrix.                                                                            
            # Finally np.diag(np.diag(self.edata*self.edata.T)) forms a diagonal matrix of solely these components         

        else:
            print("input x-y-e dimension error")

	def setParameters(self, params):
		self.linear.setPElements(params)

	def evaluate(self):
		yPred=self.linear.veval(xdata)
		diff = self.ydata-yPred
		chisq = diff.T*Icov*diff
		return chisq[0][0]

class ChiSqII:
    def __init__(self):
        print 'Evaluating a chisq'
        data = np.loadtxt("testData.txt")
        
        self.data = data 
        
        # Create Chisq object                                                                                              
        self.instance = ChiSq(matrix(data[:, 0]).T, matrix(data[:, 1]).T, matrix(data[:, 2]).T)

        # Finally form the chisq                                                                                           
        result = self.instance.evaluate()
    
        print result

