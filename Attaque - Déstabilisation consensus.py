import numpy as np
import numpy.random as npr
import matplotlib.pyplot as plt
from functools import reduce
from scipy.stats import binom
import time

"""
Idées :
    - Faire des histogrammes
    - Avoir un petit mu et tau pour le round 1 (i.e. on agrège peu de messages, et peu de personnes participent à l'agrégation), puis plus grand ensuite (pour se mettre d'accord, arriver au consensus)
    - typiquement mu*tau = 100 ; tau = 1000 ; WeightTot = 10000
    - Voir avec distribution uniforme des stakes

"""
# Paramètres

nUTXO = 250
nCommitee = 300  # nombre de votes disponibles à chaque round
nVoteMin = 200  # nombre de votes à accumuler pour envoyer un message
stake = 4
p = nCommitee / (nUTXO * stake)  #

# Processus avec agrégation uniquement au round 1

nSetIni = 1000  # S'interprête comme le nombre de sets de transactions différents après le round 1
maliciousProp = 0.2  # Proportion de noeuds malveillants
hashlist = np.arange(nSetIni)  # Pour la comparaison de 2 sets en cas d'égalité


def process(show=True):
    npr.shuffle(hashlist)
    weightList = np.ones(nSetIni)
    indexList = np.arange(nSetIni)

    i = 1
    initialSetNumber = nSetIni
    bool = False
    propEndMess = []  # proportion de messages indiquant la fin du round, par round
    survivingSets = []

    while not bool:
        weightList, indexList, countEndMess, nSurvivingSets = draw(weightList, indexList, initialSetNumber)
        i += 1
        bool = countEndMess == weightList.size
        propEndMess.append(countEndMess / weightList.size)
        survivingSets.append(nSurvivingSets)
        # print(indexlist)
        # print(i, countEndMess/weightlist.size, nSurvivingSets)
    if show:
        print("Round final: ", i, ", FinalSet : ", indexList[0], ", Nombre de sets initial : ", initialSetNumber,
              ", Nombre de sets final : ", survivingSets[-1])
    X = np.array(propEndMess)
    Y = np.array(survivingSets)
    return i, X, Y, indexList[0], survivingSets[-1]


def weightRepartition():
    l = []
    votes = npr.binomial(stake, p, nUTXO)
    for w in votes:
        if w > 0:
            l.append(w)
    # print("vote moy", np.average(l), "vote max : ", np.max(l))
    return np.array(l, dtype=int)


def draw(weightList, indexList, initialSetNumber):
    newindexlist = []
    newweightlist = weightRepartition()
    finalSet = []
    countEndMess = 0
    survivingSets = np.zeros(initialSetNumber, dtype=bool)
    # count = 0

    maliciousIndex, maliciousEndMess = maliciousBehaviour(weightList, indexList, initialSetNumber)

    for iteration in range(newweightlist.size):
        malicious = npr.binomial(1, maliciousProp) == 1

        if not malicious:
            votePerSet = np.zeros(initialSetNumber)
            voteCount = 0
            index = np.arange(weightList.size)
            npr.shuffle(index)
            i = 0
            while voteCount < nVoteMin:
                voteCount += weightList[index[i]]
                votePerSet[indexList[index[i]]] += weightList[index[i]]
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


def maliciousBehaviour(weightList, indexList, initialSetNumber):
    # soyons malicieux :
    votePerSet = np.zeros(initialSetNumber)
    voteCount = 0
    orderedVotes = []

    for i in range(weightList.size):
        votePerSet[indexList[i]] += weightList[i]

    for i in range(initialSetNumber):
        orderedVotes.append((i, votePerSet[i]))
    orderedVotes.sort(key=lambda x: x[1])

    for (i, v) in orderedVotes:
        voteCount += w
        votePerSet[i] += w
        if voteCount > nVoteMin:
            break

    kmax = 0
    # En fait ça devrait être un tableau avec les index qu'on veux favoriser, sans trop les mettre en avant non plus
    maliciousIndex = kmax
    maliciousEndMess = (1 == ((votePerSet != 0).sum()))
    return maliciousIndex, maliciousEndMess

    """
    Bon, qu'est ce qu'on fait ?
     - nombre de transactions encore en course
     - Le tableau des votes de tous les honnettes (en particulier le vote masimum pour un set)
     - 
     
    """







# Simulation d'un processus :
def simul1(n, showfrec=-1):
    I = np.zeros(n)
    X = []
    Y = []
    resultE = np.zeros(n)
    t0 = time.time()
    if showfrec == -1:
        showfrec = np.floor(n / 20)
    for i in range(n):
        a, b, c, d, e = process(show=False)
        I[i] = a
        X.append(b)
        Y.append(c)
        resultE[i] = e
        if i % showfrec == 0:
            print("Itération", i, "temps estimé avant la fin :", np.floor((time.time() - t0) * (n - i) / (i + 1)))
    print("Temps d'exécution :", np.floor(time.time() - t0))
    print(np.average(I), np.median(I), np.quantile(I, 0.25), np.quantile(I, 0.75))

    rmax = -1
    for x in X:
        if x.size > rmax:
            rmax = x.size
    resultX = np.zeros(rmax)
    resultY = np.zeros(rmax)

    for i in range(n):
        for k in range(rmax):
            if k < X[i].size:
                resultX[k] += X[i][k]
                resultY[k] += Y[i][k]
            else:
                resultX[k] += 1
                resultY[k] += 0

    resultX = resultX / n
    resultY = resultY / n
    return I, resultX, resultY, resultE


I, X, Y, E = simul1(20)
plt.hist(I, 20)
plt.show()

plt.hist(E, 20)
plt.show()

fig, (ax1, ax2) = plt.subplots(2)

ax1.plot(np.arange(2, X.size + 2, 1), X)
ax1.set_title("Proportion de messages finaux")
ax1.set_ylabel("Prop")

ax2.plot(np.arange(2, Y.size + 2, 1), Y, "r-")
ax2.set_title("Nombre de sets encore présents")
ax2.set_ylabel("Sets")
ax2.set_xlabel("Rounds")
plt.show()
