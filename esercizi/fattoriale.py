
n = input("inserire il valore di n ")

i = n
fattoriale = 1
while i > 1:
    fattoriale = fattoriale * i
    i = i - 1

print "\n %s! = " % n, fattoriale
