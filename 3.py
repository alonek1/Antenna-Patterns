from pylab import *
import matplotlib.pyplot as plt
from pylab import *
import numpy as np
theta = np.arange(-np.pi, np.pi, .01)[1:] 

def f(x):
    return x

plt.polar(theta, abs((cos(np.pi/2*cos(theta)))/sin(theta)))
show()
