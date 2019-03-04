import numpy as np
import matplotlib.pyplot as plt

# caricare i dati
fileName = 'IstatVariazionePrezzi.csv'
datiIstat = np.genfromtxt(fileName, delimiter=';', dtype=float)

# print datiIstat
# print datiIstat.shape  # tabella 50x8

# costruire la serie storica manualmente
serieStorica = np.empty([150, 2])

serieStorica[0:50, :] = datiIstat[:, 0:2]
# print serieStorica
serieStorica[50:100, :] = datiIstat[:, 3:5]
serieStorica[100:150, :] = datiIstat[:, 6:8]
# print serieStorica

# oppure in maniera automatica
for i in range(3):
    serieStorica[50 * i:50 * (i + 1), :] = datiIstat[:, (3 * i):(3 * i) + 2]
print serieStorica

# trovare la media della variazione dei prezzi
media = np.mean(serieStorica[:, 1])
print "media inclusi nan = ", media
media = np.nanmean(serieStorica[:, 1])
print "media esclusi nan = ", media


# rimuovere i valori nan
indiciNaN = np.isnan(serieStorica[:, 0])
print indiciNaN
# operatore '-' non più accettato usare '~' (tilde) o logical_not
serieStoricaRipulita = serieStorica[~indiciNaN]
print serieStoricaRipulita

# disegnare il grafico della serie storica
# con rappresentato il valor medio
annoPrimo = np.min(serieStoricaRipulita[:, 0])
annoUltimo = np.max(serieStoricaRipulita[:, 0])
print "serie storica dal ", annoPrimo, "al ", annoUltimo

plt.grid()
plt.xlabel('anno')
plt.ylabel('variazione')
plt.plot([annoPrimo, annoUltimo], [media, media], 'r-')
plt.plot(serieStoricaRipulita[:, 0], serieStoricaRipulita[:, 1], 'o-')
plt.show()
