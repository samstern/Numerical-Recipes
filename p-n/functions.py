"""
All functions are defined in this class. T
"""

def rho(y,x,h):
#Charge density of a p-n junction

	if x<=1:
		return 0
	elif x<=2 :
		return h
	elif x<=3:
		return -h
	else:
		return 0

def pd(y,e):
	return -e
