valore = 0.0
media = 0.0
iterazione = -1
while valore >= 0.0:
    media += valore
    iterazione += 1
    valore = float(input('inserisci un numero positivo (<0 termina esecuzione) '))

media /= iterazione
print 'il valor medio: ', media
