numero = input("inserire un numero intero positivo: ")
primo = False
contatore = 1

if numero % 2 == 0:
    primo = False
    print numero, "e' un numero pari"
else:
    divisore = 1.0
    while divisore < numero:
        divisore = contatore * 2 + 1
        quoziente = numero / (1.0 * divisore)
        resto = numero % divisore
        print "numero = ", numero, "contatore = ", contatore
        print "divisore = ", divisore, "quoziente = ", quoziente, "resto = ", resto, "\n"
        if resto == 0:
            if quoziente == 1.0:
                primo = True
            else:
                primo = False
            divisore = numero
        contatore = contatore + 1
if primo:
    print numero, "e' un numero primo"
else:
    print numero, " non e' un numero primo"
