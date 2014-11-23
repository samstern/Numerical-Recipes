"""
All functions are defined in this class. 
They are the rhs of each differential equation
"""

def rho(y,x,h):
	if x<=1:
		return 0
	elif x<=2 :
		return h
	elif x<=3:
		return -h
	else:
		return 0

def negE(y,x, electric):
	return -electric




