a = input("inserisci il valore a ")
b = input("inserisci il valore b ")
c = input("inserisci il valore c ")

if a**2 == b**2 + c**2:
    print "triangolo rettangolo\n"
elif b**2 == a**2 + c**2:
    print "triangolo rettangolo\n"
elif c**2 == a**2 + b**2:
    print "triangolo rettangolo\n"
else:
    print "non è un triangolo rettangolo\n"
