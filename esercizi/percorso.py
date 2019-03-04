import math

haltFlag = 1
lunghezza = 0
print "inserire le coordinate delle citta':"
print "un valore negativo termina l'inserimento"
xOld = input("ascissa ")
yOld = input("ordinata ")
while (haltFlag > 0):
    x = input("ascissa ")
    y = input("ordinata ")
    if(x < 0 or y < 0):
        haltFlag = 0
    else :
        deltaX = x - xOld
        deltaY = y - yOld
        lunghezza += (deltaX**2 + deltaY**2)
lunghezza = math.sqrt(lunghezza)
print "la lunghezza del percorso e' ", lunghezza
