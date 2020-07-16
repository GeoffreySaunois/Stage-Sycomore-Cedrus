import numpy as np
import numpy.random as npr
import matplotlib.pyplot as plt
from functools import reduce
import heapq as hq
from scipy.stats import binom
import time

"""
Idées :
    - Faire des histogrammes
    - Avoir un petit mu et tau pour le round 1 (i.e. on agrège peu de messages, et peu de personnes participent à l'agrégation), puis plus grand ensuite (pour se mettre d'accord, arriver au consensus)
    - typiquement mu*tau = 100 ; tau = 1000 ; WeightTot = 10000
    - Voir avec distribution uniforme des stakes

"""
##Paramètres

nUTXO = 250
nCommitee = 300    #note de votes disponibles à chaque round
nVoteMin = 4       #nombre de votes à accumuler pour envoyer un message
stake = 4
p = nCommitee/(nUTXO*stake) #


##Processus avec aggrégation uniquement au round 1

nCommitee01=1000       #s'interprête comme le nombre de sets de transactions différents après le round 1
#nVoteMin1=10         # Nombre de votes que les participants au round 1 doivent attendre avant de

def process(show=True):
    weightlist = weightRepartition()
    indexlist = np.arange(weightlist.size)
    i=1
    initialSetNumber = weightlist.size
    bool = False
    propEndMess=[]                  #proportion de messages indiquant la fin du round, par round
    survivingSets=[]

    while not bool:
        weightlist, indexlist, countEndMess, nSurvivingSets = draw(weightlist, indexlist, initialSetNumber)
        i+=1
        bool = countEndMess==weightlist.size
        propEndMess.append(countEndMess/weightlist.size)
        survivingSets.append(nSurvivingSets)
        #print(indexlist)
        # print(i, countEndMess/weightlist.size, nSurvivingSets)
    if show:
        print("Round final: ", i, ", FinalSet : ", indexlist[0], ", Nombre de sets initial : ", initialSetNumber, ", Nombre de sets final : ", survivingSets[-1])
    X = np.array(propEndMess)
    Y = np.array(survivingSets)
    return i, X, Y


def weightRepartition():
    l = []
    votes = npr.binomial(stake, p, nUTXO)
    for w in votes :
        if w>0:
            l.append(w)
    # print("vote moy", np.average(l), "vote max : ", np.max(l))
    return np.array(l, dtype=int)


# def weightRepartition(weightTot):
#     S=0
#     l = []
#     while S<weightTot:
#         w = npr.binomial(stake, p)
#         if w>0:
#             S+=w
#             l.append(w)
#     print("vote moy", np.average(l), "vote max : ", np.max(l))
#     return np.array(l, dtype=int)


def draw(weightlist, indexlist, initialSetNumber):
    newindexlist = []
    newweightlist = weightRepartition()
    finalSet = []
    countEndMess = 0
    survivingSets = np.zeros(initialSetNumber, dtype=bool)
    # count = 0
    for iteration in range(newweightlist.size):

        votePerSet = np.zeros(initialSetNumber)
        voteCount=0
        index = np.arange(weightlist.size)
        npr.shuffle(index)
        i = 0
        while voteCount < nVoteMin:
            voteCount+=weightlist[index[i]]
            votePerSet[indexlist[index[i]]] += weightlist[index[i]]
            i+=1

        newindexlist.append(votePerSet.argmax())
        countEndMess+= (1==((votePerSet!=0).sum()))
        survivingSets[newindexlist[-1]]=True
    nSurvivingSets = survivingSets.sum()
    return newweightlist, newindexlist, countEndMess, nSurvivingSets


##Simulation d'un processus :
# roundFinal, X, Y = process()
#
#
# fig, (ax1, ax2) = plt.subplots(2)
#
# ax1.plot(np.arange(2, X.size+2, 1), X)
# ax1.set_title("Proportion de messages finaux")
# ax1.set_ylabel("Prop")
#
# ax2.plot(np.arange(2, Y.size+2, 1), Y, "r-")
# ax2.set_title("Nombre de sets encore présents")
# ax2.set_ylabel("Sets")
# ax2.set_xlabel("Rounds")
# plt.show()

##Histogramme du nombre de round nécessaires au consensus

def simul1(n, showfrec=-1):
    I = np.zeros(n)
    X = []
    Y = []
    t0 = time.time()
    if showfrec==-1:
        showfrec=np.floor(n/20)
    for i in range(n):
        a, b, c = process(show=False)
        I[i] = a
        X.append(b)
        Y.append(c)
        if i%showfrec==0:
            print("Itération", i, "temps estimé avant la fin :", np.floor((time.time()-t0)*(n-i)/(i+1)))
    print("Temps d'exécution :", np.floor(time.time()-t0))
    print(np.average(I), np.median(I), np.quantile(I, 0.25), np.quantile(I, 0.75))

    rmax = -1
    for x in X:
        if x.size > rmax:
            rmax = x.size
    resultX = np.zeros(rmax)
    resultY = np.zeros(rmax)

    for i in range(n):
        for k in range(rmax):
            if k<X[i].size:
                resultX[k]+=X[i][k]
                resultY[k]+=Y[i][k]
            else :
                resultX[k]+=1
                resultY[k]+=0

    resultX = resultX/n
    resultY = resultY/n
    return I, resultX, resultY

I, X, Y = simul1(2000)
plt.hist(I, 100)
plt.show()

fig, (ax1, ax2) = plt.subplots(2)

ax1.plot(np.arange(2, X.size+2, 1), X)
ax1.set_title("Proportion de messages finaux")
ax1.set_ylabel("Prop")

ax2.plot(np.arange(2, Y.size+2, 1), Y, "r-")
ax2.set_title("Nombre de sets encore présents")
ax2.set_ylabel("Sets")
ax2.set_xlabel("Rounds")
plt.show()



##Histogrammes du nombre de votants par round et du nombre de vote total par round

# def weightRepartitionSimul():
#     n, v = 0, 0
#     votes = npr.binomial(stake, p, nUTXO)
#     for w in votes :
#         if w>0:
#             n+=1
#             v+=w
#     return n, v
#
# def simulVotes(n):
#     X = np.zeros(n)
#     Y = np.zeros(n)
#     for i in range(n):
#         a, b = weightRepartitionSimul()
#         X[i] = a
#         Y[i] = b
#     print(np.average(X), np.median(X), np.quantile(X, 0.25), np.quantile(X, 0.75))
#     print(np.average(Y), np.median(Y), np.quantile(Y, 0.25), np.quantile(Y, 0.75))
#     return X, Y
#
# X, Y = simulVotes(10000)
#
#
# fig, (ax1, ax2) = plt.subplots(2)
#
# ax1.hist(XX, 50)
# ax1.set_title("Histogramme du nombre d'UTXO par commité")
# # ax1.set_ylabel("Nombre d'UTXO")
#
#
# ax2.hist(Y, 50)
# ax2.set_title("Histogramme du nombre de votes par commité")
# # ax2.set_ylabel("Sets")
# # ax2.set_xlabel("Votes")
# plt.show()