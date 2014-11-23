
from functions import *
import numpy.fft as fft
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

	#create bins of rhos
	rhos = [rho(1,x,h[0]) for x in xs]

	#fourier transform
	trans_rho = fft.fft(rhos)

	i = np.complex(0,1)

	# multiply bu 1/ik and inverse fft
	trans_e = [np.complex(0,0) if n ==0+0j
	 else (trans_rho[n])*(1/(i*math.pi*n*0.5)) for n in range(0,len(xs))]
	e_field = fft.ifft(trans_e).real

	#
	correction = y0 - e_field[0]
	e_field = e_field+correction
	return xs, e_field*2 #why do i need to *2? write to lecturer

#-----------------------------------------------------------

def e_analytical(xs,h):
	ys = [0 for x in xs]
	for i in range(0,len(xs)):
		if xs[i] <=1:
			ys[i] = 0
		elif xs[i]<=2:
			ys[i] = h[i]*(xs[i]-1)
		elif xs[i]<=3:
			ys[i] = (h[i]*(3-xs[i]))
		else:
			ys[i] = 0

	return xs, ys

#---------------------------------------------------------

def v_analytical(xs,h):
	ys = [0 for x in xs]
	for i in range(0,len(xs)):
		if xs[i] <=1:
			ys[i]=0
		elif xs[i]<=2:
			ys[i] = -(h[i]*xs[i]*(0.5*xs[i]-1)+0.5*h[i])
		elif xs[i]<=3:
			ys[i] = -(h[i]*xs[i]*(3-0.5*xs[i]))+3.5*h[i]
		else:
			ys[i] = -h[i]

	return xs,ys



