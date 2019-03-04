N = 10

somma = 0
contatore = 0
numero = 0
while (contatore < 10):
    numero = input('inserire un valore ')
    somma += numero
    print contatore, " ",somma
    contatore = contatore + 1

media = somma / N
print media
