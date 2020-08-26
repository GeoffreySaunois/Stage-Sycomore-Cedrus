from scipy.stats import hypergeom
from scipy.stats import binom
from scipy.stats import poisson
import numpy as np
import pickle
import matplotlib.pyplot as plt

"""
On superpose pa -> log10(tau) pour plusieurs valeurs de Rmax
"""


XRmax = [96, 100, 150, 200, 400, 600, 800]
for Rmax in XRmax:
    filename = 'results/param(pa), Rmax = '+str(Rmax)+'/Xtau'
    infile = open(filename,'rb')
    Xtau = pickle.load(infile)
    infile.close()

    ##log 10 Tau
    plt.plot(Xpa, Xtau, label = '$R_{max} = $'+str(Rmax))
    plt.yscale('log')
    plt.legend()

plt.xlabel('$p^\mathcal{A}$')
plt.ylabel('$\\tau$')
plt.title('Évolution of $\\tau$ with $p^\mathcal{A}$, pour différentes valeur de $R_{max}$')
plt.show()