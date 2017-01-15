from pylab import *
import matplotlib.pyplot as plt
from pylab import *
import numpy as np
theta = np.arange(-np.pi, np.pi, .01)[1:] 


plt.polar(theta, abs((cos((np.pi/4*cos(theta))-np.pi/4))))
show()
