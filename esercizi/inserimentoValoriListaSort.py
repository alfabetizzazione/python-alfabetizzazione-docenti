CARDINALITA = 5
serie = []

i = 0
while i < CARDINALITA:
    numero = input('isnserisci un numero ')
    serie.append(numero)
    print serie
    i += 1

serie.sort()
print serie
