CARDINALITA = 10

lista_numeri = []

somma = 0.0
contatore = 0
while contatore < CARDINALITA:
    numero = input('inserisci un numero ')
    print "iterazione ", contatore
    lista_numeri += [numero]
    somma += float(numero)
    contatore += 1

media = somma / CARDINALITA

varianza2 = 0.0
contatore = 0
while contatore < CARDINALITA:
    varianza2 += ((lista_numeri[contatore] - media)**2)
    contatore += 1
varianza2 = varianza2 / (CARDINALITA-1.0)

print "media = ", media
print "varianza2 = ", varianza2
