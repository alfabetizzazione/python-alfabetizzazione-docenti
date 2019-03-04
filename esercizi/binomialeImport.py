import math as m

print "inserire i valori n e k"
n = input("n ")
k = input("k ")

binomiale = m.factorial(n) / (m.factorial(k) * m.factorial(n-k))

print "il coefficiente binomiale è ", binomiale
