from scipy.stats import hypergeom
from scipy.stats import binom
from scipy.stats import poisson
import numpy as np
import pickle
import matplotlib.pyplot as plt
import pylab as pl

"""
Exploitation de la heatmap pa, Rmax -> tau

"""

## Chargement des résultats :

print("Results loading...")

filename = 'results/heatmap/pa'
infile = open(filename,'rb')
pa = pickle.load(infile)
infile.close()

filename = 'results/heatmap/Rmax'
infile = open(filename,'rb')
Rmax = pickle.load(infile)
infile.close()

filename = 'results/heatmap/tau'
infile = open(filename,'rb')
tau = pickle.load(infile)
infile.close()

print("Loading succesfull !")

## Exploitation graphique


tau = np.log10(tau)
tau = tau[:-1, :-1]
l_pa=pa.min()
r_pa=pa.max()
l_Rmax=Rmax.min()
r_Rmax=Rmax.max()
l_tau,r_tau  = -np.abs(tau).max(), np.abs(tau).max()

figure, axes = plt.subplots()

tau = axes.pcolormesh(pa, Rmax, tau, cmap='cool') #, vmin=l_tau, vmax=r_tau, edgecolor='red')
axes.set_title('$\log_{10}(\\tau)$ en fonction de $p_\mathcal{A}$ et $R_{max}$')
plt.xlabel('$p^\mathcal{A}$')
plt.ylabel('$R_{max}$')
axes.axis([l_pa, r_pa, l_Rmax, r_Rmax])
figure.colorbar(tau)

plt.show()