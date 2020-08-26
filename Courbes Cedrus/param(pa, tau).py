from scipy.stats import hypergeom
from scipy.stats import binom
from scipy.stats import poisson
import numpy as np


"""
On détermine tous les paramètres (i.e : mumin, mumax, alpha, lambda, rmax) en fonction de pa et tau.
"""
## C1 et C3

Rmax = 100
epsilon = 10**(-15)

def paramPaTau(pa, tau, Rmax = 100, show = False, showProb = False) :

    ph = 1-pa

    # C1
    a = 0
    b = int(ph*tau)
    k = (a+b) //2
    while b-a > 1 :
        if poisson.cdf(k, ph*tau) < epsilon :
            a = k
            k = (a+b)//2
        else :
            b = k
            k = (a+b)//2
    mumax = a/tau

    # C3
    a = int(2*tau)
    b = int(tau)
    k = (a+b) //2
    while a-b > 1 :
        if poisson.sf(k, tau) < epsilon :
            a = k
            k = (a+b)//2
        else :
            b = k
            k = (a+b)//2
    mumin = a/(2*tau)

    mu = mumax

    # C2
    a = int(2*pa*tau)
    b = int(pa*tau)
    k = int((a+b) //2)
    while a-b > 1 :
        if poisson.sf(k, pa*tau) < epsilon :
            a = k
            k = (a+b)//2
        else :
            b = k
            k = (a+b)//2
    if mu > 0:
        alpha = a/(mu*tau)
    else :
        alpha = np.nan

    # Majoration de Xh1t
    pmin = (1-alpha)/2
    a = 0
    b = pmin*ph*tau
    k = (a+b) //2
    while b-a > 1 :
        if poisson.cdf(k, pmin*ph*tau) < epsilon :
            a = k
            k = (a+b)//2
        else :
            b = k
            k = (a+b)//2
    xh1t = a

    # C4
    n = (1-alpha)*mu*tau
    M = xh1t
    N = 2*mu*tau
    a = 0
    b = M
    k = (a+b)//2
    while (b-a)>1 : #tau/10**3 :
        # print(b-a)
        if hypergeom.cdf(k, N, M, n)*12000 < epsilon:
            a = k
            k = (a+b)//2
        else :
            b = k
            k = (a+b)//2
    if mu > 0:
        lbd = (a/(mu*tau))
    else :
        lbd = np.nan

    # rmax
    if lbd == 0 or np.isnan(lbd):
        rmax = np.nan
    else :
        rmax = 3 * int((alpha/lbd + 1))

    if show :
        print("tau = ", tau)
        print("mumin = ", int(10000*mumin)/100, "%")
        print("mumax = ", int(10000*mumax)/100, "%")
        print("alpha = ", int(10000*alpha)/100, "%")
        print("pmin = ", int(10000*pmin)/100, "%")
        print("xh1t = ", 100*xh1t/tau, "%")
        print("lbd = ", int(10000*lbd)/100, "%")
        print("rmax = ", rmax)
        print()
        # print("lbd*mu = ", int(10000*lbd*mu)/10000)

    if showProb :
        print("C1: ", poisson.cdf(mumax*tau, ph*tau))
        print("C2: ", poisson.sf(alpha*mu*tau, pa*tau))
        print("C3: ", poisson.sf(2*mumin*tau, tau))
        print("Xh1t: ", poisson.cdf(xh1t, pmin*ph*tau))
        print("C4: ", 12000 * hypergeom.cdf(lbd*mu*tau, N, M, n))
        print()
    return (tau, mumin, mumax, alpha, lbd, rmax)

