"""A variety of methods to solve first order ordinary differential equations.

AUTHOR:
    Jonathan Senning <jonathan.senning@gordon.edu>
    Gordon College
    Based Octave functions written in the spring of 1999
    Python version: March 2008, October 2008
"""



#from rk4 import *
import numpy 
from functions import *
from solveEquations import *
import scipy.integrate as integrate 



# solving dE/dx=p(x) is done by splitting the problem into four regions. The equation is solved for each region seperately.
if __name__ == "__main__":
    from pylab import *

    y0 = 0
    h = 2
    n = 52
    boundries = [1,2,3,4]
    x_e,e_field = electricField(y0,n,h,boundries)
    #print e_field
    #print x_e
    #x_v,volt = voltage(y0,e_field)
	

    plot(x_e,e_field)
    title( 'Solutions of $dE/dx =p(x) $y(0)=0$' )
    ylabel('E(x)')
    xlabel('x')

    show()



