import ABR as abr
import ABR_RN as abrRN
import RandomArray as ra
import matplotlib.pyplot as plt
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

    Tabr = abr.ABR()  # Albero br
    Tabrw = abr.ABR()
    Tabr_RN = abrRN.ABR_RN()  # Albero RN

    arrayOfNode = ra.randomArray(j)
    badArrayOfNode = []
    for i in range(0, j):
        badArrayOfNode.append(i + 1)

    for w in range(0, numOfRep):
        for i in range(0, j):
            startTime = timer()
            Tabr.insert(arrayOfNode[i])
            tempTimeAbr.append((timer() - startTime))

        for i in range(0, j):
            startTime = timer()
            Tabrw.insert(badArrayOfNode[i])
            tempTimeAbrWorst.append(timer() - startTime)

        for i in range(0, j):
            startTime = timer()
            Tabr_RN.insert(arrayOfNode[i])
            tempTimeabr_RN.append(timer() - startTime)

    # count += 1
    # if count % 10 == 0 or j == numOfTests or j == 0:
    if len(tempTimeAbr) == 0:
        ABRtime.append(0)
        ABRWorst.append(0)
        ABR_RNtime.append(0)
        numberOfNodes.append(0)
    else:
        tempABR = 0
        tempABRW = 0
        tempABR_RN = 0
        for i in range(0, len(tempTimeAbr)):
            tempABR += tempTimeAbr[i]
            tempABRW += tempTimeAbrWorst[i]
            tempABR_RN += tempTimeabr_RN[i]
        ABRtime.append(tempABR / len(tempTimeAbr))
        ABRWorst.append(tempABRW / len(tempTimeAbr))
        ABR_RNtime.append(tempABR_RN / len(tempTimeAbr))
        count = 0
        tempTimeAbr = []
        tempTimeAbrWorst = []
        tempTimeabr_RN = []
        numberOfNodes.append(j)
    heightABR.append(Tabr.heightRecursive(Tabr.root))
    heightABR_RN.append(Tabr_RN.heightRecursive(Tabr_RN.root))

    keyToSearch = random.randint(0, j + j/4)
    startTime = timer()
    Tabr.searchI(keyToSearch)
    timeToSearchABR.append(timer() - startTime)

    startTime = timer()
    Tabr_RN.searchI(keyToSearch)
    timeToSearchABR_RN.append(timer() - startTime)
    effective.append(j)
    # print("##########Temp variables refreshed & co.##########")

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
plt.title("Inserimento")
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
plt.title("Inserimento zoom")
plt.savefig('abrC_RN.png', dpi=100)
plt.show()


# Altezza
plt.plot(effective, heightABR_RN, label="ABR_RN")
plt.plot(effective, heightABR, label="ABR")
plt.legend()
plt.xlabel('Numero nodi')
plt.ylabel('Altezza')
plt.grid()
plt.draw()
plt.title("Altezza")
plt.savefig('Altezza Alberi', dpi=100)
plt.show()


# Ricerca
plt.plot(effective, timeToSearchABR_RN, label="ABR_RN")
plt.plot(effective, timeToSearchABR, label="ABR")
plt.legend()
plt.xlabel('Numero nodi')
plt.ylabel('Tempo di ricerca')
plt.grid()
plt.draw()
plt.title("Ricerca")
plt.savefig('Tempo di ricerca Alberi', dpi=100)
plt.show()

print("Ci abbiamo impiegato ", timer() - tempoTotale)
