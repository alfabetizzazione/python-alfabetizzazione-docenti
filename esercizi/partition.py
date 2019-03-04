import numpy as np


def swap(array, elemento1, elemento2):
    swapTmp = array[elemento1]
    array[elemento1] = array[elemento2]
    array[elemento2] = swapTmp


# A = np.random.randint(1000, size=15)
A = np.array([2, 8, 7, 1, 3, 5, 6, 4])
# A = np.array([2, 8, 7, 1, 3, 5, 4, 6])
r = len(A) - 1
p = 0
Abkup = np.copy(A)

x = A[r]
i = p - 1
for j in range(p, r):
    if A[j] <= x:
        i = i + 1
        swap(A, i, j)
        # print "\t", A
swap(A, i + 1, r)

print Abkup
print A
