CARDINALITA = 10

numero = 1
quanti = 0
while(quanti < CARDINALITA):
    if numero % 2 != 0:
        print "numero = ", numero, "quanti = ", quanti
        quanti += 1
    numero = numero + 1
