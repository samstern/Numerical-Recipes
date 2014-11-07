import numpy as np
    
#Bisection Method
	
def bisection(a,b,tol,f):
    c = (a+b)/2.0
    numsteps=0
    while (b-a)/2.0 > tol:
	    numsteps=numsteps+1
	    if f(c) == 0:
	       	return c
	    elif f(a)*f(c) < 0:
	       	b = c
	    else:
	       	a = c
	    c = (a+b)/2.0
		
    return c, numsteps
	


