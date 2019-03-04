import math as m
import matplotlib.pyplot as plt


haltFlag = 1
lunghezza = 0.0
listaX = []
listaY = []
print "inserire le coordinate delle citta':"
print "un valore negativo termina l'inserimento"
xOld = input("ascissa ")
yOld = input("ordinata ")
listaX.append(xOld)
listaY.append(yOld)
while (haltFlag > 0):
    x = input("ascissa ")
    y = input("ordinata ")
    if(x < 0.0 or y < 0.0):
        haltFlag = 0
    else:
        deltaX = x - xOld
        deltaY = y - yOld
        xOld = x
        yOld = y
        lunghezza += (deltaX**2 + deltaY**2)
        listaX.append(x)
        listaY.append(y)
lunghezza = m.sqrt(lunghezza)
print "la lunghezza del percorso e' ", lunghezza

plt.plot(listaX, listaY, 'ro')
plt.plot(listaX, listaY, 'b->')
plt.show()
