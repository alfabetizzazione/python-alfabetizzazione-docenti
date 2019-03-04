a = input("inserisci il valore a ")
b = input("inserisci il valore b ")
c = input("inserisci il valore c ")

if a > b:
    cat1 = b
    if a > c:
        cat2 = c
        ip = a
        print "a e' l'ipotenusa? "
    else:
        cat2 = a
        ip = c
        print "c e' l'ipotenusa? "
else:
    cat1 = a
    if b > c:
        cat2 = c
        ip = b
        print "b e' l'ipotenusa? "
    else:
        cat2 = b
        ip = c
        print "c e' l'ipotenusa? "
if ip**2 == cat1**2 + cat2**2:
    print "si ed è un triangolo rettangolo"
else:
    print "non è un triangolo rettangolo"
