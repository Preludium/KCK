from matplotlib import pylab as plt
import numpy as np
# example data
x = np.arange(0.1, 4, 0.1)
y = np.exp(-x)
# example variable error bar values
yerr = 0.1 + 0.1*np.sqrt(x)
plt.errorbar(x, y, yerr=yerr, errorevery=3)