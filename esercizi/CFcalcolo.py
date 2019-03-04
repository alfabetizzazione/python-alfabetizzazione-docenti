# generatore codice fiscale per nati in italia
#
# nome = 'alessandro'
# cognome = 'manzoni'
# dataNascita = '07031785'
# genere = 'M'
# comune = 'milano'
# # MNZLSN85C07F205D


def estraiCarCognome(parola):
    parola = parola.replace(' ', '')
    parola = parola.upper()
    frammentoConsonanti = ''
    frammentoVocali = ''
    for carattere in parola:
        if carattere not in ['A', 'E', 'I', 'O', 'U']:
            frammentoConsonanti += carattere
        else:
            frammentoVocali += carattere
    parolaRiordinata = frammentoConsonanti + frammentoVocali + 'XXX'
    # print parolaRiordinata
    return parolaRiordinata[:3]


def estraiCarNome(parola):
    parola = parola.replace(' ', '')
    parola = parola.upper()
    frammentoConsonanti = ''
    frammentoVocali = ''
    for carattere in parola:
        if carattere not in ['A', 'E', 'I', 'O', 'U']:
            frammentoConsonanti += carattere
        else:
            frammentoVocali += carattere
    if len(frammentoConsonanti) > 3:
        frammentoConsonanti = frammentoConsonanti[
            0] + frammentoConsonanti[2] + frammentoConsonanti[3]
    parolaRiordinata = frammentoConsonanti + frammentoVocali + 'XXX'
    # print parolaRiordinata
    return parolaRiordinata[:3]


def estraiCarMese(parola):
    dizionarioMesi = {'01': 'A', '02': 'B', '03': 'C', '04': 'D',
                      '05': 'E', '06': 'H', '07': 'L', '08': 'M',
                      '09': 'P', '10': 'R', '11': 'S', '12': 'T'}
    return dizionarioMesi[parola]


def estraiCarGiorno(parola, carGenere):
    if carGenere == 'F':
        giorno = int(parola) + 40
        print giorno
        parola = str(giorno)
    return parola


def estraiCarComune(parola):
    dizComuni = {}
    nomeFile = 'CFCodiceComuniItalia.csv'
    fileComuni = open(nomeFile, 'r')
    listaComuni = fileComuni.readlines()
    fileComuni.close()
    for linea in listaComuni:
        frammenti = linea.split(';')
        # print frammenti
        dizComuni[frammenti[2]] = frammenti[0]
    return dizComuni[parola.upper()]


def estraiCarControllo(parola):
    file = open('CFTabellaDispari.tsv', 'r')
    listaDispari = file.readlines()
    file.close()
    file = open('CFTabellaPari.tsv', 'r')
    listaPari = file.readlines()
    file.close()
    del listaDispari[0]
    del listaPari[0]
    dizDispari = {}
    for linea in listaDispari:
        frammenti = linea.strip().split('\t')
        for i in range(4):
            dizDispari[frammenti[2 * i]] = frammenti[2 * i + 1]
    # print dizDispari
    dizPari = {}
    for linea in listaPari:
        frammenti = linea.strip().split('\t')
        for i in range(4):
            dizPari[frammenti[2 * i]] = frammenti[2 * i + 1]
    file = open('CFTabellaResto.tsv', 'r')
    listaResto = file.readlines()
    file.close()
    dizResto = {}
    for linea in listaResto:
        frammenti = linea.strip().split('\t')
        dizResto[frammenti[0]] = frammenti[1]
    # print dizResto
    i = 0
    somma = 0
    for el in parola:
        if i % 2 == 1:  # attenzione i è indice: 0 = primo
            somma += int(dizPari[el])
            print dizPari[el]
        else:
            somma += int(dizDispari[el])
            print dizDispari[el]
        i += 1
    print 'somma = ', somma, 'resto = ', somma % 26
    car = dizResto[str(somma % 26)]
    return car

nome = raw_input('inserire il nome ')
cognome = raw_input('inserire il cognome ')
dataNascita = raw_input('inserire la data di nascita nel formato ggmmaaaa ')
genere = raw_input('inserire il genere M o F ')
comune = raw_input('inserire il comune di nascita ')

nome = nome.replace(' ', '')
print nome
cognome = cognome.replace(' ', '')
print cognome
giorno = dataNascita[:2]
print giorno
mese = dataNascita[2:4]
print mese
anno = dataNascita[6:8]
print anno, "\n"
carCognome = estraiCarCognome(cognome)
carNome = estraiCarNome(nome)
carMese = estraiCarMese(mese)
carGiorno = estraiCarGiorno(giorno, genere)
carComune = estraiCarComune(comune)
CF = carCognome + carNome + anno + carMese + carGiorno + carComune
carControllo = estraiCarControllo(CF)
CF += carControllo
print CF
