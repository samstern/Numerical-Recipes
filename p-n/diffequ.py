import numpy 
from functions import *
from solveEquations import *
import scipy.integrate as integrate 
from pylab import *


# solving dE/dx=p(x) is done by splitting the problem into four regions. The equation is solved for each region seperately.
if __name__ == "__main__":

    print "what would you like the height of the p-n junction to be? (int or float)"
    height = float(raw_input())

    print "how many steps? (int)"
    n = int(raw_input())

	#inputs
    y0 = 0
    h = [height for x in range(0,n)]
    boundry = 4 #end point
    x = numpy.linspace( y0, boundry, n)
    #want the analytical solution to always have eough points in order to compare 
    x_an = numpy.linspace(y0, boundry, 10000) 
    #find the electric field
    x_e,e_field = electricField(y0,x,h,boundry)

    #find the potential
    x_v,volt = voltage(y0,x_e,e_field,boundry)

    #fourier method to find electric fiels
    x_f,e_fourier = fourier(y0,x,h)

    #analytical solution for electric field
    real_ex, real_e = e_analytical(x,h)

    #analytical solution for potential difference
    real_vx, real_v = v_analytical(x,h)

    #errors ----------------------

    zer = [0 for i in range(0,len(x))]
    #electric field kr4 error
    e_error = [e_field[i]-real_e[i] for i in range(0,len(x))]


    #electric field fourier
    f_error = [e_fourier[i]-real_e[i] for i in range(0,len(x))]

    #potential difference error
    v_error = [volt[i]-real_v[i] for i in range(0,len(x))]

    #Root Mean Squared errors

    e_rms = math.sqrt(numpy.mean([e**2 for e in e_error]))
    f_rms = math.sqrt(numpy.mean([f**2 for f in f_error]))
    v_rms = math.sqrt(numpy.mean([v**2 for v in v_error]))
    print "\n"
    print "RMS Errors in Electric Field:"
    print "4th Order Runge-Kutta: %s"%(e_rms)
    print "Fourier Method: %s"%(f_rms)
    print "\n"
    print "RMS Errors in Potential Difference:"
    print "4th Order Runge-Kutta: %s"%(v_rms)

    #plots

    #electric field
    subplot(2,2,1)
    plot(x,real_e, 'b',x,e_field,'r',x,e_fourier,'g')
    title( r'Solutions of $\frac{dE}{dx} =\rho(x)$, n=%s, h=%s'%(n,h[0]) )
    ylabel('$E(x)$')
    xlabel('$x$')
    legend(('Analytical', 'R-K 4','Fourier'), loc='upper left')

    #electric field errors

    #potential difference
    subplot(2,2,2)
    plot(x,real_v, 'b',x,volt, 'r')
    title(r'Solutions of $\frac{dV}{dx} =-E(x)$, n=%s, h=%s'%(n,h[0]) )
    ylabel('V(x)')
    xlabel('$x$')
    legend(('Analytical',"R-K 4"), loc = 'lower left')

    subplot(2,2,3)
    plot(x,zer,'b',x,e_error,'r-+',x,f_error,'g-+')
    title('Errors in numerically calculating E')
    ylabel('error($E(x)$)')
    xlabel('$x$')
    legend(('Analytical', 'R-K 4','Fourier'), loc='lower left')

    subplot(2,2,4)
    plot(x,zer,'b',x,v_error,'r-+')
    title('Errors in numerically calculating V')
    ylabel('error($V(x)$)')
    xlabel('$x$')
    legend(('Analytical',"R-K 4"), loc = 'lower left')




    show()



