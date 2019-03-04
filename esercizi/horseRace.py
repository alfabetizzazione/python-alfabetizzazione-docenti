import numpy as np


def stampaCorsa(posizioni, cavalli):
    i = 0
    while i < cavalli:
        print "cavallo ", i, "*" * posizioni[i]
        i = i + 1
    print ""


def stampaClassifica(posizioni):
    # print posizioni.shape[0]  # equivale a len(posizioni)
    distanze = np.unique(posizioni)
    distanze = sorted(distanze)
    # print distanze, type(distanze)
    i = len(distanze) - 1
    while i >= 0:
        # print posizioni == distanze[i]
        j = 0
        while j < len(posizioni):
            if (posizioni[j] == distanze[i]):
                print len(distanze) - i, \
                    " classificato cavallo ", j, \
                    "\tcon ", posizioni[j], "\tlunghezze"
            j = j + 1
        i = i - 1


nCavalli = input("inserire il numero di cavalli che partecipano alla corsa: ")
nTurni = input("inserire il numero di turni per ogni cavallo: ")
print nCavalli, "cavalli correranno per ", nTurni, \
    "turni. Vince il cavallo che arriva più lontano"

vAvanzamenti = np.zeros(nCavalli, dtype=int)
iTurno = 0
while iTurno < nTurni:
    icavallo = 0
    while icavallo < nCavalli:
        avanzamento = np.random.randint(1, 6)
        # print avanzamento
        vAvanzamenti[icavallo] = vAvanzamenti[icavallo] + avanzamento
        icavallo = icavallo + 1
    stampaCorsa(vAvanzamenti, nCavalli)
    iTurno = iTurno + 1


stampaClassifica(vAvanzamenti)
