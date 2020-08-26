from scipy.stats import hypergeom
from scipy.stats import binom
from scipy.stats import poisson
import numpy as np

"""
Dans ce script, à pa fixé, on calcule tous les paramêtres en fonction de pa.
(i.e. : on cherche le plus petit tau tel que rmax < Rmax, puis on calcule tout)
"""

## C1 et C3

def paramPa(pa, Rmax = 100, show = False, showProb = False) :

    taumin = 0
    taumax = 10
    werein = False      # Vaut True dès que \tau \in [\tau_min, \tau_max]
    tau = taumax        # Recherche dichotomique quand on ne sait pas dans quel intervale se trouve \tau.

    while taumax - taumin > 1 :

        # print(taumax - taumin)

        (tau, mumin, mumax, alpha, lbd, rmax) = paramPaTau(pa, tau)

        if rmax > Rmax or np.isnan(rmax):      # Condition de faisabilité A : Celle qui est problématique
            if werein :
                taumin = tau
                tau = (taumin+taumax) // 2
            else :
                taumin = taumax
                taumax, tau = 2*taumax, 2*taumax
                # print("augmentation de l'intervale, cause rmax", rmax, tau)
            continue

        if alpha > 1:           # Contion B
            if werein :
                taumin = tau
                tau = (taumin+taumax) // 2
            else :
                taumin = taumax
                taumax, tau = 2*taumax, 2*taumax
                # print("augmentation de l'intervale, cause alpha", alpha, tau)
            continue

        if mumin > mumax :      # Condition C
            if werein :
                taumin = tau
                tau = (taumin+taumax) // 2
            else :
                taumin = taumax
                taumax, tau = 2*taumax, 2*taumax
                # print("augmentation de l'intervale, cause mu", mumin, mumax, tau)
            continue

                                # Quand toutes les conditions de faisabilité sont vérifiées
        taumax = tau
        tau = (taumin+taumax) // 2
        werein = True
        # print("c'est validé !")

    tau = taumax
    return paramPaTau(pa, tau, show = show, showProb = showProb)
