import random


def randomArray(size):
    a = []
    for i in range(1, size+1):
        a.append(i)
    random.shuffle(a)
    return a
