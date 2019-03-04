
def radice(numero):
    radice = 1.0
    while (radice * radice) <= numero:
        radice = radice + 1.0

    for i in range(0, 10):
        radice = 0.5 * (radice + numero / radice)
    return radice


haltFlag = 1
lunghezza = 0.0
print "inserire le coordinate delle citta':"
print "un valore negativo termina l'inserimento"
xOld = input("ascissa ")
yOld = input("ordinata ")
while (haltFlag > 0):
    x = input("ascissa ")
    y = input("ordinata ")
    if(x < 0.0 or y < 0.0):
        haltFlag = 0
    else:
        deltaX = x - xOld
        deltaY = y - yOld
        lunghezza += (deltaX**2 + deltaY**2)
lunghezza = radice(lunghezza)
print "la lunghezza del percorso e' ", lunghezza
