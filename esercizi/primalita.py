numero = input("inserire un numero intero positivo: ")
primo = False
contatore = 1
divisore = contatore * 2 + 1

while divisore <= numero:
    print "contatore ", contatore
    print "divisore ", divisore
    print "resto ", numero%divisore
    print "divisione", numero/divisore
    print numero%divisore == 0
    print "numero == divisore", numero == divisore
    print "numero mod divisore ", numero%divisore == 0
    print "check ", numero - (numero/divisore)*divisore, "\n"
    if numero == divisore:
        primo = True
    contatore = contatore + 1
    divisore = contatore * 2 + 1

if primo:
    print numero, "e' un numero primo"
else:
    print numero, "non e' un numero primo"
