import numpy as np

A = np.random.randint(10000000, size=100)
# A = np.array([5, 2, 4, 6, 1, 3])

Abkup = np.copy(A)
# print A
for j in range(1, len(A)):
    # print "j = ", j
    key = A[j]
    # print "key = ", key
    i = j - 1
    # print "i = ", i
    while i >= 0 and A[i] > key:
        A[i + 1] = A[i]
        # print "\tA[", i+1, "] = A[", i, "] = ", A[i]
        i = i - 1
        # print "\ti = ", i
        # print "\t", A
    A[i + 1] = key
    # print "A[", i, "] = ", A[i]

print Abkup
print A
