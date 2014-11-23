import numpy

def rk( f, y0, x ,args):
    """Fourth-order Runge-Kutta method to solve y' = f(y,x) with y(x[0]) = y0.

    USAGE:
        y = rk4(f, y0, x)

    INPUT:
        f     - function of y and x equal to dy/dx.  y may be multivalued,
                in which case it should a list or a NumPy array.  In this
                case f must return a NumPy array with the same dimension
                as y.
        y0    - the initial condition(s).  Specifies the value of y when
                x = x[0].  Can be either a scalar or a list or NumPy array
                if a system of equations is being solved.
        x     - list or NumPy array of x values to compute solution at.
                x[0] is the the initial condition point, and the difference
                h=x[i+1]-x[i] determines the step size h.
        args  - The arguments of function f. Must be an list at least as
                long as x.

    OUTPUT:
        y     - NumPy array containing solution values corresponding to each
                entry in x array.  If a system is being solved, y will be
                an array of arrays.
    """
    n = len( x )
    y = numpy.zeros( n )
    y[0] = y0
    for i in xrange( n - 1 ):
        h = x[i+1] - x[i]
        k1 = h * f( y[i], x[i],args[i] )
        k2 = h * f( y[i] + 0.5 * k1, x[i] + 0.5 * h, args[i] )
        k3 = h * f( y[i] + 0.5 * k2, x[i] + 0.5 * h, args[i] )
        k4 = h * f( y[i] + k3, x[i+1], args[i] )
        y[i+1] = y[i] + (( k1 + 2.0 * ( k2 + k3 ) + k4 ) / 6.0)

    return y

