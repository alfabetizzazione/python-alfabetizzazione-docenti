parola = raw_input('inserire una parola ')
# con la sintassi sotto la parola va racchiusa tra apici
# parola = input('inserire una parola racchiusa tra apici')

print parola

lettere = {}
i = 0
while i < len(parola):
    if parola[i] in lettere:
        lettere[parola[i]] += 1
    else:
        lettere[parola[i]] = 1
    i += 1

for lettera in lettere:
    print lettera, lettere[lettera]
