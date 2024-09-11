import numpy as np
np.float_ = np.float64
from intvalpy import Interval
from tabulate import tabulate


def print_table(matrix, headers):
    print(tabulate(matrix, headers, tablefmt="simple_grid", stralign='center'))


def CreateMatrix(eps):
    A = Interval([
          [[1-eps, 1+eps], [0.9-eps, 0.9+eps]],
          [[1-eps, 1+eps], [1.1-eps, 1.1+eps]]
        ])

    output = [
        [str(A[0][0]), str(A[0][1])],
        [str(A[1][0]), str(A[1][1])]
    ]

    print(f"\n---------------------------------------------------------\neps = {eps}")
    print_table(output, headers=[])

    return A


def Determinant(A):
    a = A[0][0]*A[1][1]
    b = A[0][1]*A[1][0]
    res = a - b
    print(f"\n1) A[0][0]*A[1][1] = {A[0][0]}*{A[1][1]} = {a}")
    print(f"\n2) A[0][1]*A[1][0] = {A[0][1]}*{A[1][0]} = {b}")
    print(f"\n3) A[0][0]*A[1][1] - A[0][1]*A[1][0] = {a}*{b} = {res}")
    return res


eps = 0
step = 0.01
print("STEP = ", step)

A = CreateMatrix(eps)
interval = Determinant(A)

while (0 not in interval):
    print("\ndeterminant = ", interval)
    eps += step
    A = CreateMatrix(eps)
    interval = Determinant(A)

print("\nMinimal eps = ", eps)
