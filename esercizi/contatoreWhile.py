stringa = 'si'
contatore = 0

while stringa == 'si':
    stringa = raw_input("vuoi continuare l'iterazione? si/no ")
    contatore = contatore + 1
print 'Hai eseguito ', contatore, ' iterazioni'
