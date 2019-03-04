import random as rnd
import math as m
import matplotlib.pyplot as plt

lanci = input('inserire il numero di lanci ')
numIntervalli = input('inserire il numero di intervalli in [0.0, 1.0) ')

serie = []
iLancio = []
intervalli = []

deltaIntervallo = 1.0 / float(numIntervalli)
print "larghezza intervallo", deltaIntervallo

xIntervalli = []
i = 0
while i < numIntervalli:
    intervalli.append(0.0)
    xIntervalli.append(i*deltaIntervallo)
    i += 1

xMappa = []
yMappa = []
for i in range(100):
    xMappa.append(i*1e-2)
    yMappa.append(int(m.floor(i*1e-2 / deltaIntervallo)))

i = 0
while i < lanci:
    numero = rnd.random()
    serie.append(numero)
    indiceIntervallo = int(m.floor(numero / deltaIntervallo))
    intervalli[indiceIntervallo] += 1
    iLancio.append(i)
    i += 1

frequenze = list(intervalli)

i = 0
while i < numIntervalli:
    frequenze[i] /= lanci
    i += 1

# print serie
print "\nconteggi"
for intervallo in intervalli:
    print intervallo

print "\nfrequenze"
for frequenza in frequenze:
    print frequenza

plt.figure(1)
plt.plot([0, 1], [0, 10], 'b-')
plt.plot(xMappa, yMappa, 'g.')
plt.figure(2)
plt.plot(iLancio, serie, 'ro')
plt.figure(3)
plt.bar(xIntervalli, intervalli, width=0.05, color='b')
plt.show()
