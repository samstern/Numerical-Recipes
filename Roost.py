from Bisect import *
from Newton import *
import numpy as np
import sys

true_roots_poly = [-2.49771,1.20296,3.39475]
true roots_exp = 0.693147

argv = sys.argv([1:])

tollerance = 0.00001
roots_guess = []

if len(argv) == 4:
    method = "newt"
elif len(argv) == 5:
    method = "bis"
else:
    sys.exit('wrong number of inputs. 4 for Newton, 5 for Bisection')

if method = "newt":
#Newton
    initial_n = 1
    root  = sys.argv[1]
    if sys.argv[3] = 'polynomial':
        true_root = true_roots_poly
    else:
        true_root = true_root_exp

    while np.abs(root-true_root)>tollerance:
        rootnewt(float(sys.argv[1]),int(sys.argv[2]), sys.argv[3])
