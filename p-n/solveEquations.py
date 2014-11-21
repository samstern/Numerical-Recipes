
from functions import *
import numpy
import scipy.integrate as integrate 



def electricField(y0,n,h, boundries):
	"""
Method for solving dE(x)/dx=p(x) where p is the charge density of a p-n junction

    Usage:
	y = electricField(y0,n,h,boundries)

    Input:
	y0 - the initial conditions, the value of y at x=0.
	n - the nuber of iterations for each "section" of the function
	h - the height of p(x)
	boundries - x co-ordinates of the discontinuities in p(x)

    Output:
	x - numpy array of x values
	y - values of E(x) at each point in x
	"""

	x1 = numpy.linspace( y0, boundries[0], n )
	x2 = numpy.linspace( boundries[0], boundries[1], n )
    	x3 = numpy.linspace( boundries[1], boundries[2], n )
    	x4 = numpy.linspace( boundries[2], boundries[3], n )

    	y_rk4_1 = integrate.odeint(rho,y0,x1,args=(h,))


    	y01 = y_rk4_1[-1]	# "initial condition" for second section is the value of y at the end of the first interval
    	y_rk4_2 = integrate.odeint(rho,y01,x2,args=(h,))

    	y02 = y_rk4_2[-1]
    	y_rk4_3 = integrate.odeint(rho,y02,x3,args=(h,))

    	y03 = y_rk4_3[-1]
    	y_rk4_4 = integrate.odeint(rho,y03,x4,args=(h,))

    	x = numpy.concatenate([x1,x2,x3,x4])    
    	y = numpy.concatenate([y_rk4_1,y_rk4_2,y_rk4_3,y_rk4_4])

    	return x, y[:,0]

#----------------------------------------------------------

def voltage(y0,es):

	e1 = es[0:52]#int((len(es)*0.25))-1]
	e2 = es[52:104]#[int((len(es)*0.25)):int((len(es)*0.5))-1]
	e3 = es[104:156]#[int((len(es)*0.5)):int((0.75*(len(es))))-1]
 	e4 = es[156:-1]#[int(0.75*len(es)):len(es)-1]

	y_rk4_1 = integrate.odeint(pd,y0,e1)
	print "here"
	y01 = y_rk4_1[-1]	# "initial condition" for second section is the value of y at the end of the first interval
	y_rk4_2 = integrate.odeint(pd,y01,e2)

	y02 = y_rk4_2[-1]
	y_rk4_3 = integrate.odeint(pd,y02,e3)

	y03 = y_rk4_3[-1]
	y_rk4_4 = integrate.odeint(pd,y03,e4)

	x = numpy.concatenate([e1,e2,e3,e4])    
	y = numpy.concatenate([y_rk4_1,y_rk4_2,y_rk4_3,y_rk4_4])

	return x, y

