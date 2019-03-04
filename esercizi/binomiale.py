def fattoriale(numero):
    i = numero
    prodotto = 1
    while i > 1:
        prodotto = prodotto * i
        i = i - 1
    return prodotto


print "inserire i valori n e k"
n = input("n ")
k = input("k ")

binomiale = fattoriale(n) / (fattoriale(k) * fattoriale(n-k))

print "il coefficiente binomiale è ", binomiale
