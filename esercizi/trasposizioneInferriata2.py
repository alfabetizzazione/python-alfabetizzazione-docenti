messaggio = raw_input('inserisci il messaggio ')
# messaggio = 'una frase a caso'
# messaggio = 'una frase a casos'

# CODIFICA
messaggioT = messaggio.replace(' ', '')
print messaggioT

iSpezza = (len(messaggioT) + 1) / 2

messaggioCifrato = list('#' * len(messaggioT))

for i in xrange(len(messaggioCifrato)):
    if i < iSpezza:
        messaggioCifrato[i * 2] = messaggioT[i]
    else:
        messaggioCifrato[(i - iSpezza) * 2 + 1] = messaggioT[i]

messaggioCifrato = ''.join(messaggioCifrato)
print 'messggio cifrato: ', messaggioCifrato
# DECODIFICA
iSpezza = (len(messaggioCifrato) + 1) / 2
frammento1 = ''
frammento2 = ''
for i in xrange(len(messaggioCifrato)):
    if i % 2 == 0:
        frammento1 += messaggioCifrato[i]
    else:
        frammento2 += messaggioCifrato[i]

print frammento1, frammento2

messaggioDecifrato = frammento1 + frammento2
print 'messaggio decifrato: ', messaggioDecifrato
