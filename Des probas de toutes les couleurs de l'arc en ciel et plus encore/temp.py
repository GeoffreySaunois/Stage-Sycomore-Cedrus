from scipy.stats import hypergeom
from scipy.stats import binom
from scipy.stats import poisson
import numpy as np
import pickle
import matplotlib.pyplot as plt
import pylab as pl


## param(tau, pa)

# paramPaTau(0.33, 3000, True, True)
# paramPa(0.33, True, True)


## Faire des trucs avec pickle
# dogs_dict = [1, 3]
#
# filename = 'results/param(tau)/dogs'
# outfile = open(filename,'wb')
#
# pickle.dump(dogs_dict,outfile)
# outfile.close()
#
# infile = open(filename,'rb')
# new_dict = pickle.load(infile)
# infile.close()

def f(a, b):
    n, m = np.shape(a)
    c = np.zeros((n, m))
    for i in range(n):
        for j in range(m):
            c[i][j] = (a[i][j] ** 4 + b[i][j] ** 2) * np.exp(-a[i][j] ** 2 - b[i][j] ** 2)
    return c

import numpy as np
import matplotlib.pyplot as plt

b, a = np.meshgrid(np.linspace(0, 5, 10), np.linspace(0,5, 5))

c = f(a, b)
c = c[:-1, :-1]
l_a=a.min()
r_a=a.max()
l_b=b.min()
r_b=b.max()
l_c,r_c  = -np.abs(c).max(), np.abs(c).max()

figure, axes = plt.subplots()

c = axes.pcolormesh(a, b, c, cmap='cool') #, vmin=l_c, vmax=r_c, edgecolor='red')
axes.set_title('Heatmap')
axes.axis([l_a, r_a, l_b, r_b])
figure.colorbar(c)

plt.show()