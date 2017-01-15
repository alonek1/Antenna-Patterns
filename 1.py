from pylab import *
import matplotlib.pyplot as plt
from pylab import *
import numpy as np
theta = np.arange(-np.pi, np.pi, .01)[0:] 

# def f(x):
#     return x

plt.polar(theta, abs(cos(pi*cos(theta))))
show()
