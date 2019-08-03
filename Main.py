import ABR as abr
import ABR_RN as abrRN
import RandomArray as ra
import matplotlib.pyplot as plt
import time
import random
import sys
from timeit import default_timer as timer

sys.setrecursionlimit(1000000)

print("Inserimento")
tempoTotale = timer()
ABRtime = []
ABRWorst = []
ABR_RNtime = []
badArrayOfNode = []
tempTimeAbr = []
tempTimeAbrWorst = []
tempTimeabr_RN = []
count = 0

heightABR = []
heightABRWorst = []
heightABR_RN = []
numberOfNodes = []

timeToSearchABR = []
timeToSearchABR_RN = []
numOfTests = 10000
for j in range(0, numOfTests, 50):
    print("Parliamo di ", j, "/", numOfTests, " elementi, ovvero ", j * 100 / numOfTests, "%")

    Tabr = abr.ABR()  # Albero br
    Tabrw = abr.ABR()
    Tabr_RN = abrRN.ABR_RN()  # Albero RN
    arrayOfNode = ra.randomArray(j)

    startTime = timer()
    for i in range(0, j):
        Tabr.insert(arrayOfNode[i])
    tempTimeAbr.append((timer() - startTime))

    badArrayOfNode = []
    for i in range(0, j):
        badArrayOfNode.append(i + 1)
    startTime = timer()
    for i in range(0, j):
        Tabrw.insert(badArrayOfNode[i])
    tempTimeAbrWorst.append(timer() - startTime)

    startTime = timer()
    for i in range(0, j):
        Tabr_RN.insert(arrayOfNode[i])
    tempTimeabr_RN.append(timer() - startTime)

    count += 1
    if count % 10 == 0 or j == numOfTests or j == 0:
        tempABR = 0
        tempABRW = 0
        tempABR_RN = 0
        for i in range(0, count):
            tempABR += tempTimeAbr[i]
            tempABRW += tempTimeAbrWorst[i]
            tempABR_RN += tempTimeabr_RN[i]
        ABRtime.append(tempABR / count)
        ABRWorst.append(tempABRW / count)
        ABR_RNtime.append(tempABR_RN / count)
        count = 0
        tempTimeAbr = []
        tempTimeAbrWorst = []
        tempTimeabr_RN = []
        numberOfNodes.append(j)
        heightABR.append(Tabr.heightRecursive(Tabr.root))
        heightABR_RN.append(Tabr_RN.heightRecursive(Tabr_RN.root))

        keyToSearch = random.randint(0, j*2)
        startTime = timer()
        Tabr.searchI(keyToSearch)
        timeToSearchABR.append(timer() - startTime)
        startTime = timer()
        Tabr_RN.searchI(keyToSearch)
        timeToSearchABR_RN.append(timer() - startTime)
        print("##########Temp variables refreshed & co.##########")

print(100, "%!!!!!!!")


# Inserimento: Plot con tutti e tre
plt.plot(numberOfNodes, ABR_RNtime, label="ABR_RN")
plt.plot(numberOfNodes, ABRWorst, label="ABR worst")
plt.plot(numberOfNodes, ABRtime, label="ABR")
plt.legend()
plt.xlabel('Numero Nodi')
plt.ylabel('Tempo (sec)')
plt.grid()
plt.draw()
plt.savefig('abrC_W_RN.png', dpi=100)
plt.show()

# Inserimento: Plot zoom su Abr e Abr_RN
plt.plot(numberOfNodes, ABR_RNtime, label="ABR_RN")
plt.plot(numberOfNodes, ABRtime, label="ABR")
plt.legend()
plt.xlabel('Numero Nodi')
plt.ylabel('Tempo (sec)')
plt.grid()
plt.draw()
plt.savefig('abrC_RN.png', dpi=100)
plt.show()


# Altezza
plt.plot(numberOfNodes, heightABR_RN, label="ABR_RN")
plt.plot(numberOfNodes, heightABR, label="ABR")
plt.legend()
plt.xlabel('Numero nodi')
plt.ylabel('Altezza')
plt.grid()
plt.draw()
plt.savefig('Altezza Alberi', dpi=100)
plt.show()


# Ricerca
plt.plot(numberOfNodes, timeToSearchABR_RN, label="ABR_RN")
plt.plot(numberOfNodes, timeToSearchABR, label="ABR")
plt.legend()
plt.xlabel('Numero nodi')
plt.ylabel('Tempo di ricerca')
plt.grid()
plt.draw()
plt.savefig('Tempo di ricerca Alberi', dpi=100)
plt.show()

print("Ci abbiamo impiegato ", time.time() - tempoTotale)
