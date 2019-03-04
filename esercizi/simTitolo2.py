import numpy as np
import matplotlib.pyplot as plt


def estraiPiu(valoreTitolo):
    rndNumero = np.random.random()
    # print "\t", rndNumero
    if rndNumero < 0.5:
        valoreTitolo *= 1.03
    elif rndNumero < 0.8:
        valoreTitolo *= 0.99
    else:
        valoreTitolo *= 1.0
    return valoreTitolo


def estraiMeno(valoreTitolo):
    rndNumero = np.random.random()
    # print "\t", rndNumero
    if rndNumero < 0.3:
        valoreTitolo *= 1.02
    elif rndNumero < 0.5:
        valoreTitolo *= 0.98
    else:
        valoreTitolo *= 1.0
    return valoreTitolo


def estraiUguale(valoreTitolo):
    rndNumero = np.random.random()
    # print "\t", rndNumero
    if rndNumero < 0.5:
        valoreTitolo *= 1.01
    else:
        valoreTitolo *= .99
    return valoreTitolo


lanci = input('inserire il numero di giorni ')

serieTitolo = np.empty(lanci)
serieTitolo[0] = 1.0
serieTitolo[1] = estraiUguale(serieTitolo[0])
for lancio in xrange(2, lanci):
    segno = serieTitolo[lancio - 2] - serieTitolo[lancio - 1]
    if segno < 0.0:
        serieTitolo[lancio] = estraiMeno(serieTitolo[lancio - 1])
    elif segno > 0.0:
        serieTitolo[lancio] = estraiPiu(serieTitolo[lancio - 1])
    else:
        serieTitolo[lancio] = estraiUguale(serieTitolo[lancio - 1])
    # print lancio + 1, "\t", serieTitolo[lancio + 1]

serieSegni = serieTitolo[1:] - serieTitolo[:-1]
nPiu = serieSegni[serieSegni > 0].size
freqPiu = nPiu / float(lanci - 1)
nMeno = serieSegni[serieSegni < 0].size
freqMeno = nMeno / float(lanci - 1)
nUguale = serieSegni[serieSegni == 0].size
freqUguale = nUguale / float(lanci - 1)

print freqPiu, freqMeno, freqUguale
print freqPiu + freqMeno + freqUguale

plt.grid()
plt.xlabel('giorno')
plt.ylabel('valore')
plt.plot(serieTitolo, 'o-')
plt.show()
