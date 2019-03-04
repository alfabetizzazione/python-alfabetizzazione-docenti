import numpy as np
import timeit


def insertionSort(array, elStart, elStop):
    for j in range(elStart + 1, elStop):
        key = array[j]
        i = j - 1
        while i >= 0 and array[i] > key:
            array[i + 1] = array[i]
            i = i - 1
        array[i + 1] = key


def swap(array, elemento1, elemento2):
    swapTmp = array[elemento1]
    array[elemento1] = array[elemento2]
    array[elemento2] = swapTmp


def partition(array, p, r):
    x = array[r]
    # print "\n", array, "p ", p, "r ", r, "x", x
    i = p - 1
    for j in range(p, r):
        if array[j] <= x:
            i = i + 1
            swap(array, i, j)
            # print "\t", A
    swap(array, i + 1, r)
    return i + 1  # nuovo indice del valore pivot


def quickSort(array, p, r):
    # print "\tp", p, "q =  ", "r = ", r, array
    if p < r:
        q = partition(array, p, r)
        # print "\tp", p, "q =", q, "r = ", r, array
        quickSort(array, p, q - 1)
        quickSort(array, q + 1, r)


# A = np.array([2, 8, 7, 1, 3, 5, 6, 4])
A = np.random.randint(10000000, size=10000)
Abkup = np.copy(A)
# print A
start = timeit.default_timer()
insertionSort(A, 0, len(A) - 1)
endIns = timeit.default_timer()
quickSort(Abkup, 0, len(A) - 1)
endQuick = timeit.default_timer()
print "insertionSort time = ", endIns - start
print "quickSort time = ", endQuick - endIns

# print A
