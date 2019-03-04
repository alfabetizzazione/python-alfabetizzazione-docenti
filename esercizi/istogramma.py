import random as rnd
import math as m

lanci = input('inserire il numero di lanci ')
numIntervalli = input('inserire il numero di intervalli in [0.0, 1.0) ')

serie = []
intervalli = []

deltaIntervallo = 1.0 / float(numIntervalli)
print "larghezza intervallo", deltaIntervallo

i = 0
while i < numIntervalli:
    intervalli.append(0.0)
    i += 1

i = 0
while i < lanci:
    numero = rnd.random()
    indiceIntervallo = int(m.floor(numero / deltaIntervallo))
    intervalli[indiceIntervallo] += 1
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
