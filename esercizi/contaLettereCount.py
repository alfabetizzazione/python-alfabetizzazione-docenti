parola = raw_input('inserire una parola ')
# con la sintassi sotto la parola va racchiusa tra apici
# parola = input('inserire una parola racchiusa tra apici')

print parola

lettere = {}

i = 0
while i < len(parola):
    if parola[i] not in lettere:
        lettere[parola[i]] = parola.count(parola[i])

i = 0
for carattere in lettere:
    print carattere, " ", lettere[carattere]
