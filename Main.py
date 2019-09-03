import ABR as abr
import ABR_RN as abrRN
import RandomArray as ra
import matplotlib.pyplot as plt
import random
import sys
from timeit import default_timer as timer
import time

sys.setrecursionlimit(1000000)

print("Inserimento")
tempoTotale = timer()
ABRtime = []
ABRWorst = []
ABR_RNtime = []
ABR_RNwtime = []
badArrayOfNode = []
tempTimeAbr = []
tempTimeAbrWorst = []
tempTimeabr_RN = []
tempTimeabr_RNw = []
effective = []

heightABR = []
heightABRWorst = []
heightABR_RN = []
numberOfNodes = []

timeToSearchABR = []
timeToSearchABR_RN = []
numOfTests = 1000
numOfRep = 100
for j in range(0, numOfTests, 100):
    print("Parliamo di ", j, "/", numOfTests, " elementi, ovvero ", j * 100 / numOfTests, "%")

    Tabr = abr.ABR()  # Albero BR
    Tabrw = abr.ABR()
    Tabr_RN = abrRN.ABR_RN()  # Albero RN
    Tabr_RNw = abrRN.ABR_RN()

    arrayOfNode = ra.randomArray(j)
    badArrayOfNode = []
    for i in range(0, j):
        badArrayOfNode.append(i)

    for w in range(0, numOfRep):
        for i in range(0, j):
            startTime = time.time()
            Tabr.insert(arrayOfNode[i])
            tempTimeAbr.append((time.time() - startTime))

        for i in range(0, j):
            startTime = time.time()
            Tabrw.insert(badArrayOfNode[i])
            tempTimeAbrWorst.append(time.time() - startTime)

        for i in range(0, j):
            startTime = time.time()
            Tabr_RN.insert(arrayOfNode[i])
            tempTimeabr_RN.append(time.time() - startTime)

        for i in range(0, j):
            startTime = time.time()
            Tabr_RNw.insert(badArrayOfNode[i])
            tempTimeabr_RNw.append(time.time() - startTime)

    if len(tempTimeAbr) == 0:
        ABRtime.append(0)
        ABRWorst.append(0)
        ABR_RNtime.append(0)
        ABR_RNwtime.append(0)
        numberOfNodes.append(0)
    else:
        tempABR = 0
        tempABRW = 0
        tempABR_RN = 0
        tempABR_RNw = 0
        for i in range(0, len(tempTimeAbr)):
            tempABR += tempTimeAbr[i]
            tempABRW += tempTimeAbrWorst[i]
            tempABR_RN += tempTimeabr_RN[i]
            tempABR_RNw += tempTimeabr_RNw[i]
        ABRtime.append(tempABR / len(tempTimeAbr))
        ABRWorst.append(tempABRW / len(tempTimeAbr))
        ABR_RNtime.append(tempABR_RN / len(tempTimeAbr))
        ABR_RNwtime.append(tempABR_RNw / len(tempTimeAbr))
        count = 0
        numberOfNodes.append(len(tempTimeAbr))
        tempTimeAbr = []
        tempTimeAbrWorst = []
        tempTimeabr_RN = []
        tempTimeabr_RNw = []

    keyToSearch = random.randint(0, j + j/4)
    startTime = timer()
    Tabr.searchI(keyToSearch)
    timeToSearchABR.append(timer() - startTime)

    startTime = timer()
    Tabr_RN.searchI(keyToSearch)
    timeToSearchABR_RN.append(timer() - startTime)
    effective.append(j)

print(100, "%!!!!!!!")

# Inserimento: Peggiore
plt.plot(numberOfNodes, ABR_RNwtime, label="Albero Rosso-Nero")
plt.plot(numberOfNodes, ABRWorst, label="Albero Binario worst case")
plt.legend()
plt.xlabel('Numero Nodi')
plt.ylabel('Tempo (sec)')
plt.grid()
plt.draw()
plt.title("Inserimento nel caso peggiore Albero binario")
plt.savefig('inserimenti_peggiori.png', dpi=100)
plt.show()

# Inserimento: medi
plt.plot(numberOfNodes, ABR_RNtime, label="Albero Rosso-Nero")
plt.plot(numberOfNodes, ABRtime, label="Albero Binario")
plt.legend()
plt.xlabel('Numero Nodi')
plt.ylabel("Tempo (sec)")
plt.grid()
plt.draw()
plt.title("Inserimento casi medi")
plt.savefig('inserimenti_medi.png', dpi=100)
plt.show()

# Ricerca
plt.plot(numberOfNodes, timeToSearchABR_RN, label="Albero Rosso-Nero")
plt.plot(numberOfNodes, timeToSearchABR, label="Albero Binario")
plt.legend()
plt.xlabel('Numero nodi')
plt.ylabel('Tempo di ricerca (sec)')
plt.grid()
plt.draw()
plt.title("Ricerca")
plt.savefig('Tempo_di_ricerca', dpi=100)
plt.show()

print("Ci abbiamo impiegato ", timer() - tempoTotale)
