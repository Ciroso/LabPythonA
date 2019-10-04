import math
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

tempHeightABR = []
tempHeightABR_RN = []

heightABR = []
heightABRWorst = []
heightABR_RN = []
numberOfNodes = []

tempTimeToSearchABR = []
tempTimeToSearchABR_RN = []

timeToSearchABR = []
timeToSearchABR_RN = []

numOfTests = 5000
numOfRep = 5
for j in range(0, numOfTests + 1, 1000):
    print("Parliamo di ", j, "/", numOfTests, " elementi, cioè ", j * 100 / numOfTests, "%")

    Tabr = abr.ABR()  # Albero BR
    Tabrw = abr.ABR()
    Tabr_RN = abrRN.ABR_RN()  # Albero RN
    Tabr_RNw = abrRN.ABR_RN()

    for w in range(0, numOfRep):
        arrayOfNode = ra.randomArray(j)
        badArrayOfNode = []
        for i in range(0, j):
            badArrayOfNode.append(i)

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

            # Ricerca ABR
            keyToSearch = random.randint(0, math.ceil(j + j / 4))
            startTime = timer()
            Tabr.searchI(keyToSearch)
            tempTimeToSearchABR.append(timer() - startTime)

            # Ricerca ABR_RN
            startTime = timer()
            Tabr_RN.searchI(keyToSearch)
            tempTimeToSearchABR_RN.append(timer() - startTime)

            # Altezza
            tempHeightABR.append(Tabr.heightRecursive(Tabr.root))
            tempHeightABR_RN.append(Tabr_RN.heightRecursive(Tabr_RN.root))

    if len(tempTimeAbr) == 0:
        ABRtime.append(0)
        ABRWorst.append(0)
        ABR_RNtime.append(0)
        ABR_RNwtime.append(0)
        timeToSearchABR.append(0)
        timeToSearchABR_RN.append(0)
        heightABR.append(0)
        heightABR_RN.append(0)
    else:
        tempABR = 0
        tempABRW = 0
        tempABR_RN = 0
        tempABR_RNw = 0
        tempSearchAbr = 0
        tempSearchAbr_rn = 0
        tempHABR = 0
        tempHABR_RN = 0
        for i in range(0, len(tempTimeAbr)):
            tempABR += tempTimeAbr[i]
            tempABRW += tempTimeAbrWorst[i]
            tempABR_RN += tempTimeabr_RN[i]
            tempABR_RNw += tempTimeabr_RNw[i]
            tempSearchAbr += tempTimeToSearchABR[i]
            tempSearchAbr_rn += tempTimeToSearchABR_RN[i]
            tempHABR += tempHeightABR[i]
            tempHABR_RN += tempHeightABR_RN[i]
        ABRtime.append(tempABR / len(tempTimeAbr))
        ABRWorst.append(tempABRW / len(tempTimeAbrWorst))
        ABR_RNtime.append(tempABR_RN / len(tempTimeabr_RN))
        ABR_RNwtime.append(tempABR_RNw / len(tempTimeabr_RNw))
        timeToSearchABR.append(tempSearchAbr / len(tempTimeToSearchABR))
        timeToSearchABR_RN.append(tempSearchAbr_rn / len(tempTimeToSearchABR_RN))
        heightABR.append(tempHABR / len(tempHeightABR))
        heightABR_RN.append(tempHABR_RN / len(tempHeightABR_RN))

        tempTimeAbr = []
        tempTimeAbrWorst = []
        tempTimeabr_RN = []
        tempTimeabr_RNw = []
        tempTimeToSearchABR = []
        tempTimeToSearchABR_RN = []
        tempHeightABR = []
        tempHeightABR_RN = []

    numberOfNodes.append(j)

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

# Altezza
plt.plot(numberOfNodes, heightABR_RN, label="Altezza Albero Rosso-Nero")
plt.plot(numberOfNodes, heightABR, label="Altezza Albero Binario")
plt.legend()
plt.xlabel('Altezza')
plt.ylabel('Nodi')
plt.grid()
plt.draw()
plt.title("Altezza")
plt.savefig('Altezza', dpi=100)
plt.show()
