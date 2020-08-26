from scipy.stats import hypergeom
from scipy.stats import binom
from scipy.stats import poisson
import numpy as np
import pickle
import matplotlib.pyplot as plt

## Exploitation graphique de param(tau) à pa fixé

Rmax = 96

print("Results loading...")

if not os.path.exists('results/param(pa), Rmax = '+str(Rmax)):
    print("Calculs pas encore faits pour cette valeur de Rmax...")
    print("Loading failure :(")
else :
    filename = 'results/param(pa), Rmax = '+str(Rmax)+'/Xtau'
    infile = open(filename,'rb')
    Xtau = pickle.load(infile)
    infile.close()

    filename = 'results/param(pa), Rmax = '+str(Rmax)+'/Xmumin'
    infile = open(filename,'rb')
    Xmumin = pickle.load(infile)
    infile.close()

    filename = 'results/param(pa), Rmax = '+str(Rmax)+'/Xmumax'
    infile = open(filename,'rb')
    Xmumax = pickle.load(infile)
    infile.close()

    filename = 'results/param(pa), Rmax = '+str(Rmax)+'/Xalpha'
    infile = open(filename,'rb')
    Xalpha = pickle.load(infile)
    infile.close()

    filename = 'results/param(pa), Rmax = '+str(Rmax)+'/Xlbd'
    infile = open(filename,'rb')
    Xlbd = pickle.load(infile)
    infile.close()

    filename = 'results/param(pa), Rmax = '+str(Rmax)+'/Xr'
    infile = open(filename,'rb')
    Xr = pickle.load(infile)
    infile.close()

    print("Loading succesfull !")

    ##Tau
    plt.plot(Xpa, Xtau, label = '$\\tau$')
    plt.legend()

    plt.xlabel('$p^\mathcal{A}$')
    plt.ylabel('$\\tau$')
    plt.title('Évolution of $\\tau$ with $p^\mathcal{A}$')
    plt.show()

    ##log 10 Tau
    plt.plot(Xpa, Xtau, label = '$\\tau$')
    plt.yscale('log')
    plt.legend()

    plt.xlabel('$p^\mathcal{A}$')
    plt.ylabel('$\\tau$')
    plt.title('Évolution of $\\tau$ with $p^\mathcal{A}$')
    plt.show()

    ## Mu
    plt.plot(Xpa, Xmumin, label = '$\\mu_{min}$')
    plt.plot(Xpa, Xmumax, label = '$\\mu_{max} = \\mu$')
    plt.legend()

    plt.xlabel('$p^\mathcal{A}$')
    plt.ylabel('$\\mu_{min}$ and $\\mu_{max}$')
    plt.title('Évolution of $\\mu_{min}$ and $\\mu_{max}$ with $p^\mathcal{A}$')
    plt.show()

    ## Alpha
    plt.plot(Xpa, Xalpha, label = '$\\alpha$')
    plt.legend()

    plt.xlabel('$p^\mathcal{A}$')
    plt.ylabel('$\\alpha$')
    plt.title('Évolution of $\\alpha$ with $p^\mathcal{A}$')
    # plt.ylim(np.min(Xalpha), 2)
    plt.show()

    ## lbd

    plt.plot(Xpa, Xlbd, label = '$\\lambda$')
    plt.legend()

    plt.xlabel('$p^\mathcal{A}$')
    plt.ylabel('$\\lambda$')
    plt.title('Évolution of $\\lambda$ with $p^\mathcal{A}$')
    plt.show()

    ## rmax
    plt.plot(Xpa, Xr, label = '$r_{max}$')
    plt.legend()

    plt.xlabel('$p^\mathcal{A}$')
    plt.ylabel('$r_{max}$')
    plt.title('Évolution of $r_{max}$ with $p^\mathcal{A}$')
    # plt.ylim(np.min(Xr[imin:])/2, 300)
    plt.show()
