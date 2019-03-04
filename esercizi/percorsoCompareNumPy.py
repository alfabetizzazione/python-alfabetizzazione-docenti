import math as m
import numpy as np
import random as raand
import timeit

numCitta = input("inserire il numero di città ")

x = raand.sample(xrange(1000000), numCitta)
y = raand.sample(xrange(1000000), numCitta)

start = timeit.default_timer()
i = 1
lunghezza = 0.0
while i < numCitta:
    deltaX = x[i] - x[i - 1]
    deltaY = y[i] - y[i - 1]
    lunghezza += (deltaX**2 + deltaY**2)
    i = i + 1
lunghezza = m.sqrt(lunghezza)

stopOld = timeit.default_timer()
npX = np.array(x)
npY = np.array(y)

npDeltaX = npX[1:] - npX[:-1]
npDeltaY = npY[1:] - npY[:-1]
npLunghezza = np.sqrt(np.sum(npDeltaX**2 + npDeltaY**2))
stopNP = timeit.default_timer()

print "la lunghezza del percorso e' \n", lunghezza
print npLunghezza

print "timing old = ", stopOld - start, "\ntiming  NP = ", stopNP - stopOld