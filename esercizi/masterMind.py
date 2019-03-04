import numpy as np

CODICE = {0: '+', 1: '*', 2: '0',
          3: '#', 4: '$', 5: '&'}
TENTATIVI = 9
DIMSegreto = 4


def generaSegreto():  # genera la stringa da indovinare
    serie = np.random.randint(0, 5, DIMSegreto)
    stringa = ''
    for el in serie:
        stringa += CODICE[el]
    return stringa


def eliminaCol(stringa, lIndici):  # elimina colori dalla stringa
    if len(lIndici) > 0:
        nuovaStringa = ''
        indice = 0
        j = 0
        while indice < len(stringa):
            if indice != lIndici[j]:
                nuovaStringa += stringa[indice]
            else:
                if j < len(lIndici) - 1:
                    j += 1
            indice += 1
        return nuovaStringa
    else:
        return stringa


def verificaGiocata(soluzione, solSegreta):
    # restituisce la lista
    # [valida,
    #  colori giusti posto corretto,
    #  colori giusto posto errato]
    valida = True
    colCorr = 0
    colErr = 0
    if len(soluzione) == DIMSegreto:  # lunghezza sol potrebbe essere sbagliata
        # verifico quanti sono colori sono in posizione corretta
        i = 0
        indCorr = []
        for el in soluzione:
            if el in CODICE.values():  # se colore valido
                if el == solSegreta[i]:
                    colCorr += 1
                    # se col ok lo tolgo da sol per non contarlo in colErr
                    indCorr.append(i)
            else:
                valida = False
            i += 1
        # elimino colori corretti per non includerli nel conteggio di quelli
        # nella posizione errata
        soluzione = eliminaCol(soluzione, indCorr)
        solSegreta = eliminaCol(solSegreta, indCorr)
        if valida and colCorr < 4:
            i = 0
            for el in soluzione:
                j = 0
                while j < len(solSegreta):
                    if el == solSegreta[j]:
                        colErr += 1
                        solSegreta = solSegreta[:j] + solSegreta[j + 1:]
                        # eliminaCol(solSegreta, [j])  # per non contare 2
                        # volte stesso colore
                    j += 1
    else:  # lunghezza sol sbagliata
        valida = False
    responso = [valida, colCorr, colErr]
    return responso


segreto = generaSegreto()
# segreto = '#*$+'
# segreto = '$*+*'
print 'per giocare devi inserire una stringa di 4 simboli scelti tra '
for el in CODICE:
    print CODICE[el]
print 'sono possibili ripetizioni'

tentativo = 0
solCorretta = False
while tentativo < TENTATIVI and solCorretta == False:
    print '\ntentativo ', tentativo + 1
    giocata = raw_input('inserisci una soluzione ')
    confronto = verificaGiocata(giocata, segreto)
    if confronto[0] == False:
        print 'Soluzione non valida riprova'
        tentativo -= 1
    print 'Colori corretti al posto corretto ', confronto[1]
    print 'Colori corretti al posto errato   ', confronto[2]
    if confronto[1] == len(segreto):
        solCorretta = True
    tentativo += 1
if confronto[1] == len(segreto):
    print 'Hai vinto'
else:
    print 'i colori erano: ', segreto
