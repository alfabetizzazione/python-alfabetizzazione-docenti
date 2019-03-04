import numpy as np


def stampaCorsa(posizioni, cavalli):
    for i in range(cavalli):
        print "cavallo ", i, "*" * posizioni[i]
    print ""


def stampaClassifica(posizioni):
    # print posizioni.shape[0]  # equivale a len(posizioni)
    distanze = np.unique(posizioni)
    distanze = sorted(distanze)
    # print distanze, type(distanze)
    i = len(distanze) - 1
    while i >= 0:
        # print (posizioni == distanze[i])
        for j in range(len(posizioni)):
            if (posizioni[j] == distanze[i]):
                print len(distanze) - i, \
                    " classificato cavallo ", j, \
                    "\tcon ", posizioni[j], "\tlunghezze"
        i = i - 1


nCavalli = input("inserire il numero di cavalli che partecipano alla corsa: ")
nTurni = input("inserire il numero di turni per ogni cavallo: ")
print nCavalli, "cavalli correranno per ", nTurni, \
    "turni. Vince il cavallo che arriva piu' lontano"

vAvanzamenti = np.zeros(nCavalli, dtype=int)

for iTurno in range(nTurni):
    icavallo = 0
    for icavallo in range(nCavalli):
        avanzamento = np.random.randint(1, 6)
        # print avanzamento
        vAvanzamenti[icavallo] = vAvanzamenti[icavallo] + avanzamento
    stampaCorsa(vAvanzamenti, nCavalli)


stampaClassifica(vAvanzamenti)
