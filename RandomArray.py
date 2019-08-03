import random


def randomArray(size):
    a = []
    for i in range(0, size):
        a.append(i+1)
    random.shuffle(a)
    return a
