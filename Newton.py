import sys
import numpy as np

def polynomial(x):
    return x**3 - 2.1*x**2 - 7.4*x +10.2
def exponential(x):
    return np.exp(x)-2
	
def poly_prime(x):
    return 3*x**2 - 4.2*x - 7.4
def exp_prime(x):
    return np.exp(x)

def newt(x,n, function):
     if function == 'polynomial':
        f = lambda x: polynomial(x)
        f_prime = lambda x:poly_prime(x)
     elif function == "exponential":
        f = lambda x: exponential(x)
        f_prime = lambda x: exp_prime(x)
     else:
        sys.exit('<function> must be either polynomial or exponential')
     for i in range(n):
        if f_prime(x) == 0:
            return x
        x = x - f(x)/f_prime(x)
     return x
	
def main(argv):
	if (len(sys.argv) != 4):
		sys.exit('Usage: newtons_method.py <x> <n> <function>')
	
	print 'The root is: ',
	print newt(float(sys.argv[1]),int(sys.argv[2]), sys.argv[3])

if __name__ == "__main__":
	main(sys.argv[1:])
