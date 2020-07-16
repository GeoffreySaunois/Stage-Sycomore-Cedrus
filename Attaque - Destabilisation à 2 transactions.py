import numpy as np
import numpy.random as npr
import matplotlib.pyplot as plt
from numpy.core._multiarray_umath import ndarray
import time

votesTot: int = 3000        # tau
votesTooSee: int = np.int(votesTot*2/3)     # mu*tau / et d'après ma remarque quant au risque d'abstention des malhonnêtes, on devrait même choisir une valeur plus faible
nMalicious: int = 850                      # np.int(np.floor(votesTot/3))
nHonest: int = votesTot - nMalicious
# On suppose que les malveillants représentent un tier du réseau, et qu'il y en a exactement votesTot/3 par round qui ont le droits de voter

# Voir que que donne cette simu si l'on ajoute des variations du nombre de vote par round / nombre de malveillants tirés à chaque round

# On suppose ici que tous les utilisateurs ont des votes égaux à 1, ce qui est souvent le cas avec un tau faible

def processRound1():
    setsInCourse = np.arange(3000)
    honestSets = honestDrawRound1(setsInCourse)
    maliciousSets = maliciousDrawRound1(honestSets)
    setsInCourse = np.concatenate((honestSets, maliciousSets))
    analyse(honestSets)
    analyse(setsInCourse)
    for itération in range(10):
        honestSets = honestDraw(setsInCourse)
        maliciousSets = maliciousDrawRound1(honestSets)
        setsInCourse = np.concatenate((honestSets, maliciousSets))
        analyse(honestSets)
        analyse(setsInCourse)

    return None


def honestDrawRound1(setsInCourse):
    nHonest: int = np.int(np.ceil(votesTot*2/3))
    honestSets = np.zeros(nHonest, dtype=int)
    for people in range(nHonest):
        # votesPerSet = np.zeros(votesTot)     # On suppose qu'il y a votesTot sets au départ
        npr.shuffle(setsInCourse)
        argmin = votesTot+1
        for setIndex in range(votesTooSee):
            if setsInCourse[setIndex]<argmin:
                argmin = setsInCourse[setIndex] # On utilise les index des sets comme leur hash
        honestSets[people] = argmin
    return honestSets

def honestDraw(setsInCourse):
    honestSets = np.zeros(nHonest, dtype=int)
    for people in range(nHonest):
        votesPerSet = np.zeros(votesTot)     # On suppose qu'il y a votesTot sets au départ
        npr.shuffle(setsInCourse)
        for setIndex in range(votesTooSee):
            votesPerSet[setsInCourse[setIndex]] += 1

        argmax: int = 0
        for k in range(1, votesPerSet.size):
            if votesPerSet[k] > votesPerSet[argmax]:
                argmax = k

        honestSets[people] = argmax
    return honestSets


def analyse(setsInCourse):
    votesPerSets = np.zeros(votesTot, dtype=int)

    for seti in setsInCourse:
        # print(seti)
        votesPerSets[seti] += 1

    X = []
    Y = []
    for k in range(votesPerSets.size):
        if votesPerSets[k] > 0:
            X.append(k)
            Y.append(votesPerSets[k])
    # plt.plot(X, Y)
    # plt.show()
    print(X, Y)
    return None


def maliciousDrawRound1(honestSets):
    honestVotesPerSets = np.zeros(votesTot, dtype=int)

    for seti in honestSets:
        # print(seti)
        honestVotesPerSets[seti] += 1

    X = []
    Y = []
    for k in range(honestVotesPerSets.size):
        if honestVotesPerSets[k] > 0:
            X.append(k)
            Y.append(honestVotesPerSets[k])

    if len(X) > 1:
        firstargmax = 0
        secondargmax = 1
        if Y[secondargmax] > Y[firstargmax]:
            firstargmax, secondargmax = secondargmax, firstargmax
            # print("Évènement improbable 1")
        for k in range(2, len(X)):
            if Y[k] > Y[secondargmax]:
                # print("Évènement improbable 2")
                if Y[k] > Y[firstargmax]:
                    # print("Évènement improbable 3")
                    firstargmax, secondargmax = k, firstargmax
                else:
                    secondargmax = k
        maliciousSets = np.zeros(nMalicious, dtype=int)
        for k in range(nMalicious):
            if k < (nMalicious + Y[firstargmax] - Y[secondargmax]) / 2:
                maliciousSets[k] = X[secondargmax]
            else:
                maliciousSets[k] = X[firstargmax]
    else:
        maliciousSets = np.ones(nMalicious, dtype=int)*np.int(X[0]+1)
    return maliciousSets


processRound1()


