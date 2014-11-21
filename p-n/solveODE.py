from numpy import * ;
from matplotlib.pyplot import *
import math as mt

#================================================================
# Convenience Class to hold a set of [y,t] pairs for each step. 
# Main purpose is to produce 1-D lists suitable for plotting from the fundamental list of pars fo ordinates     
class ResultSet:
    def __init__(self):
        self.results = [ ]
      
    def add(self, pair ):
        self.results.append(pair)
     
    def get(self, i ):
        if( (i<0) or (i>len(self.results)) ):
            print ' index out of range '
            return [0.,0.]
        return self.results[i] 
        
    def getAll(self):
        return self.results
        
    def yvalues(self):
        yvalues = [ y for [y,t] in self.results ]
        return yvalues
        
    def tvalues(self):
        tvalues = [ t for [y,t] in self.results ]
        return tvalues
        
    def printIt(self):
        print self.results
        
#================================================================
# These are ODE classes to hold all of the problem information

# Exponential ODE dy/dy = k * y
class MyODEExponential:
    def __init__(self, _k):
        print 'Creating MyODE: Exponential'
        self.k = _k
        self.initial = [ self.exactSolution(0.), 0. ]
        
    # The derivative is particularly simple    
    def firstDerivative(self, pair ):
        return self.k*pair[0]
        
    # Initil values are part of the ODE infomration    
    def initialValue(self):
        return self.initial
    
    # This exact solution is given to compare accuracy            
    def exactSolution(self, t):
        return mt.exp(self.k*t)
        
        
# Polynomial ODE with arbitrary coeficients: y = c[0] +c[1]*x +c[2]*x^2 + c[3]*x^3 .....
class MyODEPolynomial:
    def __init__(self, _coeffs ):
        print 'Creating MyODE: Polynomial'
        self.coeffs = _coeffs 
        self.initial = [self.exactSolution(-0.), -0.]
        
    def firstDerivative(self, pair ):
        val = 0.
        for power in range(len(self.coeffs)-1):
            val+= (power+1)*self.coeffs[power+1]*mt.pow(pair[1],float(power))
        return val
        
    def initialValue(self):
        return self.initial
        
    def exactSolution(self, t):
        val = 0.
        for power in range(len(self.coeffs)):
            val+= self.coeffs[power]*mt.pow(t,float(power))
        return val
        
# Sinusoid ODE with period omega
class MyODESinusoid:
    def __init__(self, omega ):
        print 'Creating MyODE: Sinusoid'
        self.omega = omega
        self.initial = [self.exactSolution(0.), 0.]
        
    def firstDerivative(self, pair ):
        return cos( self.omega*pair[1] )
        
    def initialValue(self):
        return self.initial
        
    def exactSolution(self, t):
        return sin( self.omega*t )
        
    
#========================================================================
# These are three different ways to do the integration steps, in ascending sophistication
 
class StepEuler:
    def dy( self, ode, pair, dt ):
        dy = ode.firstDerivative( pair ) * dt 
        return [ dy, dt ]
        

class StepRK0:
    def dy( self, ode, pair, dt ):
        midpoint = [ pair[0]+ ode.firstDerivative( pair ) * dt/2, pair[1]+dt/2 ]
        dy = ode.firstDerivative( midpoint ) * dt 
        return [ dy, dt ]
        
        
class StepRK:
    def dy( self, ode, pair, dt ):
        y = pair[0]
        t = pair[1]        
        d1 = ode.firstDerivative( [y,t] )
        d2 = ode.firstDerivative( [y+ dt/2*d1, t+dt/2 ] )
        d3 = ode.firstDerivative( [y+ dt/2*d2, t+dt/2 ] )
        d4 = ode.firstDerivative( [y+ dt*d3, t+dt ] )
        dy = dt*(1./6.)*(d1 + 2*d2 + 2*d3 + d4)
        return [ dy, dt ]
        

#============================================================================        
# Engine to do the work
class Engine:
    def __init__(self, ode, step, title ):
        self.ode = ode 
        self.step = step
        self.title =  title
        
    def go(self, nsteps, dt ):
    
        resultSet = ResultSet( )
        resultSet.add( self.ode.initialValue() )

        for i in range(nsteps):
            current = resultSet.get( i )
            change = self.step.dy( self.ode, current, dt )
            next = [ current[0]+change[0], current[1]+change[1] ]
            resultSet.add( next)
                    
        print ' Engine Finished for '+self.title
        return resultSet

                        
#==================================================================
# Guiding program

def main(nsteps=-1, delta=0, type=''):

        
    print ' Running ODE integration for ', type, ' with nsteps = ',nsteps,'  and dt = ',delta

    #Create ODE
    if( type == 'poly' ):
        ode = MyODEPolynomial([ 1., 1., -3., 1. ] )
#        ode = MyODEPolynomial([ 10.2, -7.42, -2.1, 1. ] )
    elif( type == 'exp' ):
        ode = MyODEExponential(1. )
    elif( type == 'sin' ):
        ode = MyODESinusoid( 1. )
    else:
        print ' No functional form specified: ', type
        quit()
        
    #Create Euler step machine
    eulerStep = StepEuler( )
    eulerEngine = Engine( ode, eulerStep, ' Exponential with Euler integration ') 
    
    #Create RK0 step machine
    rk0Step = StepRK0( )
    rk0Engine = Engine( ode, rk0Step, ' Exponential with RK-0 integration ') 
    
    #Create RK step machine
    rkStep = StepRK( )
    rkEngine = Engine( ode, rkStep, ' Exponential with RK integration ') 
    
    #run them
    resultSetEuler = eulerEngine.go(nsteps, delta)
    resultSetRK0 = rk0Engine.go(nsteps, delta)
    resultSetRK = rkEngine.go(nsteps, delta)
        
    yvaluesEuler = resultSetEuler.yvalues() 
    yvaluesRK0 = resultSetRK0.yvalues()
    yvaluesRK = resultSetRK.yvalues()
    tvalues = resultSetRK.tvalues() 
