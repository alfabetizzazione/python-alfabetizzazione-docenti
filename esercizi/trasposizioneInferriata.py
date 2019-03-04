messaggio = raw_input('inserisci il messaggio ')
# messaggio = 'una frase a caso'
# messaggio = 'una frase a casos'

# CODIFICA
messaggioT = messaggio.replace(' ', '')
print messaggioT

iSpezza = (len(messaggioT) + 1) / 2
print 'len = ', len(messaggioT), 'iSpezza', iSpezza
stringa1 = messaggioT[:iSpezza]
stringa2 = messaggioT[iSpezza:]
print stringa1, len(stringa1)
print stringa2, len(stringa2)
lMessaggioCifrato = list(messaggioT)

for i in xrange(iSpezza):
    indice = i * 2
    print indice
    lMessaggioCifrato[indice] = stringa1[i]
    print ' ', indice + 1
    if i < len(stringa2):
        lMessaggioCifrato[indice + 1] = stringa2[i]

messaggioCifrato = ''.join(lMessaggioCifrato)
print messaggioCifrato

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
print messaggioDecifrato
