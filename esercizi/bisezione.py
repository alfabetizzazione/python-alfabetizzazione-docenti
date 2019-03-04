ITERAZIONI = 100

# def effe(x):
#     y = - x + 2.0
#     return y
def effe(x):
    y = x**3 - 13 * x**2 + 19 * x + 33
    return y


# listaPunti[0] = Xmin
# listaPunti[1] = Xmid
# listaPunti[2] = Xmax
def intervallo(listaPunti):
    if(effe(listaPunti[0]) * effe(listaPunti[1]) <= 0):
        listaPunti[2] = listaPunti[1]  # Xmax = Xmid
    else:
        listaPunti[0] = listaPunti[1]  # Xmin = Xmid
    listaPunti[1] = 0.5 * (listaPunti[0] + listaPunti[2])


a = 0.0
b = 9.0

listaX = [a, 0.5 * (a + b), b]
print listaX
i = 0
while (i < ITERAZIONI):
    intervallo(listaX)
    print listaX
    i = i + 1
