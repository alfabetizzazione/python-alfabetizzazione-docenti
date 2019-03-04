def trova_lettera(word, substring):
    indice = word.find(substring)
    return indice


parola = raw_input('inserire una parola ')
# con la sintassi sotto la parola va racchiusa tra apici
# parola = input('inserire una parola racchiusa tra apici')
lettera = raw_input('inserire la lettera da cercare ')

posizione = 0
indici = []
while posizione < len(parola):
    nuovo_indice = trova_lettera(parola[posizione:], lettera)
    if nuovo_indice != -1:
        indici += [nuovo_indice + posizione]
        posizione += nuovo_indice + len(lettera)
    else:
        posizione = len(parola)

if indici != []:
    for indice in indici:
        print indice
else:
    print "lettera non trovata"