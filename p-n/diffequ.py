import numpy 
from functions import *
from solveEquations import *
import scipy.integrate as integrate 



# solving dE/dx=p(x) is done by splitting the problem into four regions. The equation is solved for each region seperately.
if __name__ == "__main__":
    from pylab import *

    y0 = 0
    n = 1000
    h = [1 for x in range(0,n)]
    boundry = 4
    x = numpy.linspace( y0, boundry, n)

    #find the electric field
    x_e,e_field = electricField(y0,x,h,boundry)

    #find the potential
    x_v,volt = voltage(y0,x_e,e_field,boundry)

    x_f,e_fourier = fourier(y0,x,h)

    plot(x_f,e_fourier)
    title( 'Solutions of $dE/dx =p(x) $y(0)=0$' )
    ylabel('E(x)')
    xlabel('x')

    show()



