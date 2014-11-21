
from functions import *
import numpy.fft as fft
import scipy.integrate as integrate 
from Runge_Kutta import *
import math
import numpy as np





def electricField(y0,x,h, boundry):

	y = rk(rho, y0, x,h)
	return x, y

#----------------------------------------------------------

def voltage(y0,x,e_field,boundry):

	y = rk(negE,y0,x,e_field)
	return x, y

#----------------------------------------------------------

def fourier(y0,xs,h):

	rhos = [rho(1,x,h[0]) for x in xs]
	trans_rho = fft.fft(rhos)
	i = np.complex(0,1)
	print i
	trans_e = [np.complex(0,0) if n ==0+0j
	 else (trans_rho[n])*(1/(i*math.pi*n*0.5)) for n in range(0,len(xs))]
	e_field = fft.ifft(trans_e)

	correction = 0- e_field[0]
	e_field = e_field+correction
	return xs, e_field*2 #why do i need to *2? write to lecturer