from scipy.stats import hypergeom
from scipy.stats import binom
from scipy.stats import poisson
import numpy as np
import pickle
import os

"""
À pa constant, on regarde l'évolution des paramètres en fonction de tau, et si les conditions sont vérifiées :
alpha < 1
mumin < mumax
rmax < Rmax

Ceci permet notamment de déterminer le facteur limitant, pour pa fixé.
"""

## Courbes des facteurs limitant


pa = 0.1
taumax = paramPa(pa)[0]
Xtau = np.linspace(100, taumax*3/2, 1000)

Xmumin, Xmumax, Xalpha, Xlbd, Xr = np.zeros(len(Xtau)), np.zeros(len(Xtau)), np.zeros(len(Xtau)) ,np.zeros(len(Xtau)), np.zeros(len(Xtau))

for i in range(len(Xtau)) :
    print("\rRunning... " + str(int(100*i/len(Xtau))) + "\t%", end="")
    (tau, mumin, mumax, alpha, lbd, rmax) = paramPaTau(pa, Xtau[i])
    Xmumin[i] = (mumin)
    Xmumax[i] = (mumax)
    Xalpha[i] = (alpha)
    Xlbd[i] = (lbd)
    Xr[i] = (rmax)
print("\rDone !")

## Sauve les donnés dans un fichier

print("Results backup...")

if not os.path.exists('results/param(tau), pa='+str(pa)):
    os.makedirs('results/param(tau), pa='+str(pa))

filename = 'results/param(tau), pa='+str(pa)+'/Xtau'
outfile = open(filename,'wb')
pickle.dump(Xtau, outfile)
outfile.close()

filename = 'results/param(tau), pa='+str(pa)+'/Xmumin'
outfile = open(filename,'wb')
pickle.dump(Xmumin, outfile)
outfile.close()

filename = 'results/param(tau), pa='+str(pa)+'/Xmumax'
outfile = open(filename,'wb')
pickle.dump(Xmumax, outfile)
outfile.close()

filename = 'results/param(tau), pa='+str(pa)+'/Xalpha'
outfile = open(filename,'wb')
pickle.dump(Xalpha, outfile)
outfile.close()

filename = 'results/param(tau), pa='+str(pa)+'/Xlbd'
outfile = open(filename,'wb')
pickle.dump(Xlbd, outfile)
outfile.close()

filename = 'results/param(tau), pa='+str(pa)+'/Xr'
outfile = open(filename,'wb')
pickle.dump(Xr, outfile)
outfile.close()

print("Backup succesfull !")

