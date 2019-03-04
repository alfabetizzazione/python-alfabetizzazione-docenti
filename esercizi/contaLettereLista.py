parola = raw_input('inserire una parola ')
# con la sintassi sotto la parola va racchiusa tra apici
# parola = input('inserire una parola racchiusa tra apici')

print parola

lettereCarattere = []
lettereConteggio = []
i = 0
while i < len(parola):
    if parola[i] in lettereCarattere:
        j = 0
        while j < len(lettereCarattere):
            if parola[i] == lettereCarattere[j]:
                lettereConteggio[j] += 1
            j += 1
    else:
        lettereCarattere.append(parola[i])
        lettereConteggio.append(1)
    i += 1

i = 0
while i < len(lettereCarattere):
    print lettereCarattere[i], ' ', lettereConteggio[i]
    i += 1
