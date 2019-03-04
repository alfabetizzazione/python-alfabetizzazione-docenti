CARDINALITA = 10


somma = 0.0
somma_quadrati = 0.0

contatore = 0
while contatore < CARDINALITA:
    numero = input('inserisci un numero ')
    print "iterazione ", contatore
    somma += float(numero)
    somma_quadrati += float(numero)**2
    contatore += 1

media = somma / CARDINALITA
varianza = (somma_quadrati - (somma**2 / CARDINALITA)) / (CARDINALITA - 1.0)

print "media = ", media
print "varianza = ", varianza
