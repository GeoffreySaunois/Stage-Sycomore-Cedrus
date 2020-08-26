from scipy.stats import hypergeom
from scipy.stats import binom
from scipy.stats import poisson
import numpy as np
import pickle
import matplotlib.pyplot as plt
import pylab as pl

"""
Crée la heatmap pa, Rmax -> tau

Ramarque : on doit prendre pa <= 0.38 et Rmax >= 60 [paramPa crash pour (0.39, 60) ou (0.38, 50)].

"""

## Calculs
def f(a, b):
    n, m = np.shape(a)
    c = np.zeros((n, m))
    for i in range(n):
        for j in range(m):
            print("\rRunning... " + str(int(100*(i*m+j)/(n*m))) + "\t%", end="")
            c[i][j] = paramPa(pa[i][j], Rmax = Rmax[i][j])[0]
    # print(c)
    return c

Rmax, pa = np.meshgrid(np.linspace(60, 200, 20), np.linspace(0.01,0.38, 20))
tau = f(pa, Rmax)
print("\rDone !")

## Sauve les donnés dans un fichier

print("Results backup...")

if not os.path.exists('results/heatmap'):
    os.makedirs('results/heatmap')

filename = 'results/heatmap/pa'
outfile = open(filename,'wb')
pickle.dump(pa, outfile)
outfile.close()

filename = 'results/heatmap/Rmax'
outfile = open(filename,'wb')
pickle.dump(Rmax, outfile)
outfile.close()

filename = 'results/heatmap/tau'
outfile = open(filename,'wb')
pickle.dump(tau, outfile)
outfile.close()

print("Backup succesfull !")