import numpy as np
import pylab as pl
import numpy.random as rand # Random number generation module
import matplotlib.pyplot as plt 

mu, sigma = 0, 1

nums = np.random.normal(mu, sigma, 2000)

print "here"

plt.hist(nums, bins=15)
plt.show()
