a = input("Immetti il coefficiente a ")
b = input("Immetti il coefficiente b ")
c = input("Immetti il coefficiente c ")
print ("Data l'equazione algebrica " + str(a) +
       "*X^2+" + str(b) + "*X+" + str(c) + "=0 ")
delta = b * b - 4 * a * c
rad_delta = delta**0.5
x1 = -(b - rad_delta) / (2 * a)
x2 = -(b + rad_delta) / (2 * a)
print ("Le soluzioni sono: " + str(x1) + " e " + str(x2))
