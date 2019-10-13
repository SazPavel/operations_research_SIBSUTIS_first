import numpy as np


def col(col1, col2):
    restmp = []
    for it in range(len(col1)):
        if col1[it] == 0:
            restmp.append(np.inf)
        else:
            restmp.append(col2[it] / col1[it])
    return restmp


A = np.array([[1.0, -5, -4, 0, 0, 0, 0, 0],
              [0, 6, 4, 1, 0, 0, 0, 24],
              [0, 1, 2, 0, 1, 0, 0, 6],
              [0, -1, 1, 0, 0, 1, 0, 1],
              [0, 0, 1, 0, 0, 0, 1, 2]])

B = np.array([[0.0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0]])
"""
A = np.array([[1.0, -4, -6, 0, 0, 0, 0],
              [0, 2, 1, 0, 0, 0, 64],
              [0, 1, 3, 0, 1, 0, 72],
              [0, 0, 1, 0, 0, 1, 20]])
B = np.array([[0.0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0]])
"""

print("original:")
for i in range(len(A)):
    for j in range(len(A[i])):
        print('{0:5.2f}'.format(A[i, j]), end=" ")
    print()
print()

while 1:

    if min(A[0]) >= 0:
        break
    minindex = list(A[0]).index(min(A[0]))
    res = col(A[1:, minindex], A[1:, -1])

    mini = -1
    minval = np.inf
    for r in res:
        if 0 < r < minval:
            minval = r
            mini = res.index(r)
    mini += 1

    #       .___,
    #    ___('v')___
    #    `"-\._./-"'
    #        ^ ^
    for r in range(len(A[mini, :])):
        B[mini] = A[mini] / A[mini, minindex]
    for i in range(len(A)):
        if i != mini:
            B[i] = A[i] - A[i, minindex] * B[mini]
    A = np.copy(B)
    for i in range(len(B)):
        for j in range(len(B[i])):
            print('{0:5.2f}'.format(B[i, j]), end=" ")
        print()
    print()
