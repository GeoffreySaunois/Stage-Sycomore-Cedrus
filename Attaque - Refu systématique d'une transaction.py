import numpy as np
import numpy.random as npr
import matplotlib.pyplot as plt
from numpy.core._multiarray_umath import ndarray
import time

"""
Idées :
    - Faire des histogrammes
    - Avoir un petit mu et tau pour le round 1 (i.e. on agrège peu de messages, et peu de personnes participent à l'agrégation), puis plus grand ensuite (pour se mettre d'accord, arriver au consensus)
    - typiquement mu*tau = 100 ; tau = 1000 ; WeightTot = 10000
    - Voir avec distribution uniforme des stakes

"""
## Paramètres

nUTXO = 250
nCommitee = 300  # Nombre de votes disponibles à chaque round
nVoteMin = 200  # Nombre de votes à accumuler pour envoyer un message
stake = 4
p = nCommitee / (nUTXO * stake)  #

## Processus avec aggrégation uniquement au round 1

nSetIni = 1000  # S'interprête comme le nombre de sets de transactions différents après le round 1
# nRefus = 600  # Nombre de sets contenant une transaction refusée systématiquement
# maliciousProp = 0.2  # Proportion de noeuds malveillants
hashlist = np.arange(nSetIni)  # Pour la comparaison de 2 sets en cas d'égalité


def process(show=True, maliciousProp=0.2, nRefus=600):
    npr.shuffle(hashlist)
    weightlist = np.ones(nSetIni)
    indexlist = np.arange(nSetIni)

    i = 1
    initialSetNumber = nSetIni
    endOfProcess = False
    propEndMess = []  # Proportion de messages indiquant la fin du round, par round
    survivingSets = []

    while not endOfProcess:
        weightlist, indexlist, countEndMess, nSurvivingSets = \
            draw(weightlist, indexlist, initialSetNumber,
                 maliciousProp=maliciousProp, nRefus=nRefus)
        i += 1
        endOfProcess = countEndMess == weightlist.size
        propEndMess.append(countEndMess / weightlist.size)
        survivingSets.append(nSurvivingSets)
        # print(indexlist)
        # print(i, countEndMess/weightlist.size, nSurvivingSets)
    if show:
        print("Round final: ", i, ", FinalSet : ", indexlist[0], ", Nombre de sets initial : ", initialSetNumber,
              ", Nombre de sets final : ", survivingSets[-1])
    X = np.array(propEndMess)
    Y = np.array(survivingSets)
    return i, X, Y, indexlist[0]


def weightRepartition():
    weights: list = []
    votes = npr.binomial(stake, p, nUTXO)
    for w in votes:
        if w > 0:
            weights.append(w)
    # print("vote moy", np.average(l), "vote max : ", np.max(l))
    return np.array(weights, dtype=int)


def draw(weightlist, indexlist, initialSetNumber, maliciousProp=0.2, nRefus=600):
    newindexlist = []
    newweightlist = weightRepartition()
    countEndMess = 0
    survivingSets = np.zeros(initialSetNumber, dtype=bool)
    # count = 0

    # soyons malicieux :
    votePerSet = np.zeros(initialSetNumber)
    maliciousVotePerSet = np.zeros(initialSetNumber)
    voteCount = 0
    maliciousVoteCount = 0
    for i in range(weightlist.size):
        if indexlist[i] >= nRefus:
            maliciousVoteCount += weightlist[i]
            maliciousVotePerSet[indexlist[i]] += weightlist[i]
        voteCount += weightlist[i]
        votePerSet[indexlist[i]] += weightlist[i]

    if maliciousVoteCount >= nVoteMin:
        kmax = 0
        for k in range(nRefus, votePerSet.size):
            if (maliciousVotePerSet[k] > maliciousVotePerSet[kmax]) or (
                    (maliciousVotePerSet[k] == maliciousVotePerSet[kmax]) and (hashlist[k] > hashlist[kmax])):
                kmax = k
        maliciousIndex = kmax
        maliciousEndMess: bool = (1 == ((maliciousVotePerSet != 0).sum()))
    else:
        kmax = 0
        for k in range(1, votePerSet.size):
            if (votePerSet[k] > votePerSet[kmax]) or (
                    (votePerSet[k] == votePerSet[kmax]) and (hashlist[k] > hashlist[kmax])):
                kmax = k
        maliciousIndex = kmax
        maliciousEndMess: bool = (1 == ((votePerSet != 0).sum()))

    for iteration in range(newweightlist.size):
        malicious = npr.binomial(1, maliciousProp) == 1

        if not malicious:
            votePerSet = np.zeros(initialSetNumber)
            voteCount = 0
            index = np.arange(weightlist.size)
            npr.shuffle(index)
            i = 0
            while voteCount < nVoteMin:
                voteCount += weightlist[index[i]]
                votePerSet[indexlist[index[i]]] += weightlist[index[i]]
                i += 1
            kmax = 0
            for k in range(1, votePerSet.size):
                if (votePerSet[k] > votePerSet[kmax]) or (
                        (votePerSet[k] == votePerSet[kmax]) and (hashlist[k] > hashlist[kmax])):
                    kmax = k
            newindexlist.append(kmax)
            countEndMess += (1 == ((votePerSet != 0).sum()))
            survivingSets[newindexlist[-1]] = True
        else:
            newindexlist.append(maliciousIndex)
            countEndMess += maliciousEndMess

    nSurvivingSets = survivingSets.sum()
    return newweightlist, newindexlist, countEndMess, nSurvivingSets


# Trace uniquement l'histogramme des trasaction entre 0 et 1000, afin de visualiser l'action de l'adversaire
# (Il y a moins de transactions entre 0 et 600 que entre 600 et 1000)
def simul1(n, showfrec=-1, maliciousProp=0.2, nRefus=600, show=False):
    sf: ndarray = np.zeros(n)
    t0 = time.time()
    if showfrec == -1:
        showfrec = np.floor(n / 20)
    for i in range(n):
        sf[i] = process(show=False, maliciousProp=maliciousProp, nRefus=nRefus)[3]
        if show and i % showfrec == 0:
            print("\rItération", i, "temps estimé avant la fin de ce calcul :",
                  np.floor((time.time() - t0) * (n - i) / (i + 1)), end='')
    # if show:
    #     print("Temps d'exécution :", np.floor(time.time() - t0))

    return sf


# SF = simul1(100)
# plt.hist(SF, 100)
# plt.show()

# Trace la courbe de la probabilité que le bloc suivant contienne la transacction ciblée, en fonction de la proportion de malveillants
def simul2(maliciousProps, nbPerPoint):
    propInfluencedTrx = np.zeros(maliciousProps.size)
    t0 = time.time()
    for iteration in range(maliciousProps.size):
        nRefus: int = np.int((1-maliciousProps[iteration])*nSetIni)
        print("Calcul pour une proportion de :", maliciousProps[iteration], "avec", nRefus, "transactions refusées (", iteration, "sur", maliciousProps.size,
              ")")
        SF = simul1(nbPerPoint, showfrec=1, maliciousProp=maliciousProps[iteration], nRefus=nRefus, show=True)
        count = 0
        for transactionIndex in SF:
            if transactionIndex >= nRefus:
                count += 1
        propInfluencedTrx[iteration] = count / nbPerPoint
        print("\rRésultat:", propInfluencedTrx[iteration])
        print("Temps restant estimé :",
              np.floor((time.time() - t0) *
                       (maliciousProps.size - iteration) / (iteration + 1)))
    return propInfluencedTrx


malProps = np.logspace(-4, np.log10(0.33), 3)
pit = simul2(malProps, 1000)

plt.plot(malProps, pit)
