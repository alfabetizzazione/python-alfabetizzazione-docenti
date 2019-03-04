
def swap(lista, elemento1, elemento2):
    swapTmp = lista[elemento1]
    lista[elemento1] = lista[elemento2]
    lista[elemento2] = swapTmp


def partition(lista, p, r):
    x = lista[r]
    # print "\n", lista, "p ", p, "r ", r, "x", x
    i = p - 1
    for j in range(p, r):
        if lista[j] <= x:
            i = i + 1
            swap(lista, i, j)
            # print "\t", A
    swap(lista, i + 1, r)
    return i + 1  # nuovo indice del valore pivot


def quickSort(lista, p, r):
    # print "\tp", p, "q =  ", "r = ", r, lista
    if p < r:
        q = partition(lista, p, r)
        # print "\tp", p, "q =", q, "r = ", r, lista
        quickSort(lista, p, q - 1)
        quickSort(lista, q + 1, r)


A = [2, 8, 7, 1, 3, 5, 6, 4]

Abkup = list(A)
print A
quickSort(A, 0, len(A) - 1)
print A
