from scipy.stats import hypergeom
from scipy.stats import binom
from scipy.stats import poisson
import numpy as np
import pickle
import matplotlib.pyplot as plt

## Exploitation graphique de param(tau) à pa fixé

pa = 0.1


print("Results loading...")

if not os.path.exists('results/param(tau), pa='+str(pa)):
    print("Calculs pas encore faits pour cette valeur de pa...")
    print("Loading failure :(")
else :
    filename = 'results/param(tau), pa='+str(pa)+'/Xtau'
    infile = open(filename,'rb')
    Xtau = pickle.load(infile)
    infile.close()

    filename = 'results/param(tau), pa='+str(pa)+'/Xmumin'
    infile = open(filename,'rb')
    Xmumin = pickle.load(infile)
    infile.close()

    filename = 'results/param(tau), pa='+str(pa)+'/Xmumax'
    infile = open(filename,'rb')
    Xmumax = pickle.load(infile)
    infile.close()

    filename = 'results/param(tau), pa='+str(pa)+'/Xalpha'
    infile = open(filename,'rb')
    Xalpha = pickle.load(infile)
    infile.close()

    filename = 'results/param(tau), pa='+str(pa)+'/Xlbd'
    infile = open(filename,'rb')
    Xlbd = pickle.load(infile)
    infile.close()

    filename = 'results/param(tau), pa='+str(pa)+'/Xr'
    infile = open(filename,'rb')
    Xr = pickle.load(infile)
    infile.close()

    print("Loading succesfull !")

    ## Mu
    plt.plot(Xtau, Xmumin, label = '$\\mu_{min}$')
    plt.plot(Xtau, Xmumax, label = '$\\mu_{max}$')
    plt.legend()

    plt.fill_between(Xtau, min(np.min(Xmumin), np.min(Xmumax)), max(np.max(Xmumin), np.max(Xmumax)), where= (Xmumax>=Xmumin), color='#cbffba')
    plt.fill_between(Xtau, min(np.min(Xmumin), np.min(Xmumax)), max(np.max(Xmumin), np.max(Xmumax)), where= (Xmumax<Xmumin), color='#ffb8b8')

    i = 0
    while Xmumin[i] > Xmumax[i]:
        i += 1
    taumu = int(Xtau[i])

    plt.text(taumu, 0.5, '$\\tau_{\\mu} =$'+str(taumu))
    plt.xlabel('$\\tau$')
    plt.ylabel('$\\mu_{min}$ and $\\mu_{max}$')
    plt.title('Évolution of $\\mu_{min}$ and $\\mu_{max}$ with $\\tau$')
    plt.show()

    ## Alpha
    plt.plot(Xtau, Xalpha, label = '$\\alpha$')
    plt.plot(Xtau, np.ones(len(Xtau)))
    plt.legend()

    plt.fill_between(Xtau, 0, max(2, np.max(Xalpha)), where= (Xalpha<1), color='#cbffba')
    plt.fill_between(Xtau, 0, max(2, np.max(Xalpha)), where= (Xalpha>=1), color='#ffb8b8')

    i = 0
    while Xalpha[i] > 1:
        i += 1
    taualpha = int(Xtau[i])

    plt.text(taualpha, np.min(Xalpha)+0.05, '$\\tau_{\\alpha} =$'+str(taualpha))

    plt.xlabel('$\\tau$')
    plt.ylabel('$\\alpha$')
    plt.title('Évolution of $\\alpha$ with $\\tau$')
    # plt.xlim(100, 5000)
    plt.ylim(np.min(Xalpha), max(min(np.max(Xalpha) ,2), 1.1))
    plt.show()

    ## lbd

    plt.plot(Xtau, Xlbd, label = '$\\lambda$')
    plt.legend()

    plt.xlabel('$\\tau$')
    plt.ylabel('$\\lambda$')
    plt.title('Évolution of $\\lambda$ with $\\tau$')
    # plt.xlim(100, 5000)
    plt.show()

    ## rmax
    plt.plot(Xtau, Xr, label = '$r_{max}$')
    plt.legend()

    imin = 0
    while np.isnan(Xr[imin]):
        imin += 1

    plt.plot(Xtau[imin:], Rmax*np.ones(len(Xtau)-imin))
    plt.fill_between(Xtau, 0, np.max(Xr[imin:]), where= (Xr<Rmax), color='#cbffba')
    plt.fill_between(Xtau, 0, np.max(Xr[imin:]), where= (Xr>=Rmax), color='#ffb8b8')

    i = imin
    while np.isnan(Xr[i]) or Xr[i] > Rmax:
        i += 1
        # print(Xr[i])
    taur = int(Xtau[i])
    plt.text(taur, Rmax +10, '$\\tau_{r_{max}} =$'+str(taur))

    plt.xlabel('$\\tau$')
    plt.ylabel('$r_{max}$')
    plt.title('Évolution of $r_{max}$ with $\\tau$')
    # plt.xlim(10000, 14000)
    plt.ylim(np.min(Xr[imin:])/2, 300)
    plt.show()