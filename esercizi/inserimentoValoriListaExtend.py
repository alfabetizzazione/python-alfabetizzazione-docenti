CARDINALITA = 5
serie = []
serie2 = ['terzultimo', 'penultimo', 'ultimo']

i = 0
while i < CARDINALITA:
    numero = input('isnserisci un numero ')
    serie.append(numero)
    print serie
    i += 1
serie.extend(serie2)
print serie