import matplotlib.pyplot as plt
from pylab import *
import numpy as np
theta = np.arange(0, 2*np.pi, .01)[1:] 
plt.polar(theta, abs(sin(theta)))
show()
