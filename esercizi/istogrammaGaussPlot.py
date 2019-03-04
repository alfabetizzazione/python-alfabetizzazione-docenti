import random as rnd
import math as m
import matplotlib.pyplot as plt


def estrazione(lista, nLanci):
    i = 0
    while i < nLanci:
        numero = rnd.gauss(5, 1)
        serie.append(numero)
        i += 1
    return lista


def minMax(lista):
    min = float('inf')
    max = -float('inf')
    for el in lista:
        if (el < min):
            min = el
        if (el > max):
            max = el
    return [min, max]


def istogramma(lista, conteggi, min, deltaInt):
    for el in lista:
        indiceIntervallo = int(m.floor((el - numeroMinMax[0]) / deltaIntervallo))
        conteggi[indiceIntervallo] += 1

lanci = input('inserire il numero di lanci ')
numIntervalli = input('inserire il numero di intervalli ')



serie = []
estrazione(serie, lanci)

numeroMinMax = minMax(serie)
print "valore minimo = ", numeroMinMax[0], "valore massimo = ", numeroMinMax[1]
deltaIntervallo = (numeroMinMax[1] - numeroMinMax[0]) / float(numIntervalli)
print "larghezza intervallo", deltaIntervallo

conteggioIntervallo = []
xIntervalli = []
i = 0
while i <= numIntervalli:  # un intervallo in più per contenere MAX
    conteggioIntervallo.append(0.0)
    xIntervalli.append(i*deltaIntervallo + numeroMinMax[0])
    i += 1


istogramma(serie, conteggioIntervallo, numeroMinMax[0], deltaIntervallo)
del conteggioIntervallo[-1]  # per eliminare il numero massimo
del xIntervalli[-1]

frequenze = list(conteggioIntervallo)
i = 0
while i < numIntervalli:
    frequenze[i] /= lanci
    i += 1


iLancio = range(lanci)

plt.figure(1)
plt.plot(iLancio, serie, 'ro')
plt.figure(2)
plt.bar(xIntervalli, conteggioIntervallo, width=deltaIntervallo, color='b')
plt.show()