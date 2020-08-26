from scipy.stats import hypergeom
from scipy.stats import binom
from scipy.stats import poisson
import numpy as np
import matplotlib.pyplot as plt
import pickle

"""
On trace l'evolution de tous les paramêtres en fonction de pa (en choisissant le tau optimal à chaque fois)
"""
Rmax = 800
## Coubes des paramètres en fonction de pa

Xpa = np.linspace(0.01, 0.41, 1000)

Xtau, Xmumin, Xmumax, Xalpha, Xlbd, Xr = np.zeros(len(Xpa)), np.zeros(len(Xpa)), np.zeros(len(Xpa)), np.zeros(len(Xpa)) ,np.zeros(len(Xpa)), np.zeros(len(Xpa))
for i in range(len(Xpa)) :
    print("\rRunning... " + str(int(100*i/len(Xpa))) + "\t%", end="")
    (tau, mumin, mumax, alpha, lbd, rmax) = paramPa(Xpa[i], Rmax = Rmax)
    Xtau[i] = (tau)
    Xmumin[i] = (mumin)
    Xmumax[i] = (mumax)
    Xalpha[i] = (alpha)
    Xlbd[i] = (lbd)
    Xr[i] = (rmax)
print("\rDone !")


## Sauve les donnés dans un fichier

print("Results backup...")

if not os.path.exists('results/param(pa), Rmax = '+str(Rmax)):
    os.makedirs('results/param(pa), Rmax = '+str(Rmax))

filename = 'results/param(pa), Rmax = '+str(Rmax)+'/Xpa'
outfile = open(filename,'wb')
pickle.dump(Xpa, outfile)
outfile.close()

filename = 'results/param(pa), Rmax = '+str(Rmax)+'/Xtau'
outfile = open(filename,'wb')
pickle.dump(Xtau, outfile)
outfile.close()

filename = 'results/param(pa), Rmax = '+str(Rmax)+'/Xmumin'
outfile = open(filename,'wb')
pickle.dump(Xmumin, outfile)
outfile.close()

filename = 'results/param(pa), Rmax = '+str(Rmax)+'/Xmumax'
outfile = open(filename,'wb')
pickle.dump(Xmumax, outfile)
outfile.close()

filename = 'results/param(pa), Rmax = '+str(Rmax)+'/Xalpha'
outfile = open(filename,'wb')
pickle.dump(Xalpha, outfile)
outfile.close()

filename = 'results/param(pa), Rmax = '+str(Rmax)+'/Xlbd'
outfile = open(filename,'wb')
pickle.dump(Xlbd, outfile)
outfile.close()

filename = 'results/param(pa), Rmax = '+str(Rmax)+'/Xr'
outfile = open(filename,'wb')
pickle.dump(Xr, outfile)
outfile.close()

print("Backup succesfull !")
