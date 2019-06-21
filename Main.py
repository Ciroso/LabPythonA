import ABR as abr
import ABR_RN as abrRN
import RandomArray as ra
import matplotlib.pyplot as plt
import time
import numpy as np

print("cane: Inserimento")

size = 50

tempoTotale = time.time()
ABRtime = []
ABRpeggiore = []
ABR_RNtime = []
badArrayOfNode = []
numOfTests = 100
count=0
for j in range(0, numOfTests,20):
    print("Parliamo di ", j, "/", numOfTests, "%", j*100/numOfTests)  # , end=' e ci mette ')
    #arrayOfNode = ra.randomArray(size*j)
    #for i in range(0, size*j):
     #   badArrayOfNode.append(i)

    Tabr = abr.ABR()            # Radice albero br
    Tabr_RN = abrRN.ABR_RN()    # Radice albero RN

    for i in range(0, size*j):
        arrayOfNode = ra.randomArray(size * j)
        startTime = time.time()
        Tabr.insert(arrayOfNode[i])
        ABRtime.append((time.time() - startTime))
        count += 1

    for i in range(0, size*j):
        for k in range(0, size * j):
            badArrayOfNode.append(k)
        startTime = time.time()
        Tabr.insert(badArrayOfNode[i])
        ABRpeggiore.append(time.time() - startTime)

    for i in range(0, size*j):
        arrayOfNode = ra.randomArray(size * j)
        startTime = time.time()
        Tabr_RN.insert(arrayOfNode[i])
        ABR_RNtime.append(time.time() - startTime)


t = np.arange(0, len(ABRtime))
print(100, "%!!!!!!!")

plt.plot(t, ABRtime, label="ABR")
plt.plot(t, ABR_RNtime, label="ABR_RN")
plt.plot(t, ABRpeggiore, linestyle='', marker='*', label="ABR worst")
plt.legend()
plt.xlabel('Numero Nodi')
plt.ylabel('Tempo (sec)')
plt.grid()
plt.draw()
plt.savefig('grafico.png', dpi=100)
plt.show()
print("Ci abbiamo impiegato ", time.time() - tempoTotale)

#T.inorder_tree_walk(T.root)
