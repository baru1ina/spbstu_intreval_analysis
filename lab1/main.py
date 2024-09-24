import numpy as np
np.float_ = np.float64
from intvalpy import Interval, mid, subset, intersection
from tabulate import tabulate


def print_table(matrix, headers):
    print(tabulate(matrix, headers, tablefmt="simple_grid", stralign='center'))


def CreateMatrix(eps):
    # A = Interval([
    #       [[1-eps, 1+eps], [0.9-eps, 0.9+eps]],
    #       [[1-eps, 1+eps], [1.1-eps, 1.1+eps]]
    #     ])

    A = Interval([
          [[1.05-eps, 1.05+eps], [0.95-eps, 0.95+eps]],
          [[1-eps, 1+eps], [1-eps, 1+eps]]
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


a = 4
eps = 0
step = 0.01
step_ = 0.0001
print("STEP = ", step)

A = CreateMatrix(eps)
interval = Determinant(A)

iter_count = 0

while 0 not in interval:
    print("\ndeterminant = ", interval)
    eps += step
    A = CreateMatrix(eps)
    interval = Determinant(A)
    iter_count += 1

while 0 in interval:
    print("\ndeterminant = ", interval)
    eps -= step_
    A = CreateMatrix(eps)
    interval = Determinant(A)
    iter_count += 1

print("iter_count", iter_count)
eps_min = round(eps+step_, a)
A = CreateMatrix(eps_min)
interval = Determinant(A)
print("\nMinimal eps = ", eps_min)

eps_max = chr(4113)
print(f"\ndiapason eps = [{eps_min}, +{eps_max}]")

output = [
    [str(A[0][0]), str(A[0][1])],
    [str(A[1][0]), str(A[1][1])]
]
print_table(output, headers=[])

print(f"\ndet(A) for minimal eps = {interval}")

# print(A[0][0])
# print(A[0][1])
# print(A[1][0])
# print(A[1][1])

step = 0.001

def CutInt(A):
    if intersection(A[0][0], A[1][0]):
        if intersection(A[1][1], A[0][1]):
            res = [
                [intersection(A[0][0], A[1][0]), intersection(A[1][1], A[0][1])],
                [intersection(A[0][0], A[1][0]), intersection(A[1][1], A[0][1])]
            ]
            return res
    if intersection(A[0][0], A[0][1]):
        if intersection(A[1][1], A[1][0]):
            res = [
                [intersection(A[0][0], A[0][1]), intersection(A[0][0], A[0][1])],
                [intersection(A[1][1], A[1][0]), intersection(A[1][1], A[1][0])]
            ]
            return res
    return None

def CalcMatrix(A):
    s1 = round(A[0][0].inf, a)
    e1 = round(A[0][0].sup, a)
    while e1 >= s1:
        s4 = round(A[1][1].inf, a)
        e4 = round(A[1][1].sup, a)
        while e4 >= s4:
            s2 = round(A[0][1].inf, a)
            e2 = round(A[0][1].sup, a)
            while s2 <= e2:
                s3 = round(A[1][0].inf, a)
                e3 = round(A[1][0].sup, a)
                while s3 <= e3:
                    if (round(e1*e4, 3) - round(s2*s3, 3)) == 0:
                        matrix = [
                            [e1, s2],
                            [s3, e4]
                        ]
                        return matrix
                    print("e1 s2 s3 e4", e1, s2, s3, e4)
                    s3 = s3 + step
                    s3 = round(s3, 3)
                print("e1 s2 s3 e4", e1, s2, s3, e4)
                s2 = s2 + step
                s2 = round(s2, 3)
            print("e1 s2 s3 e4", e1, s2, s3, e4)
            e4 = e4 - step
            e4 = round(e4, 3)
        print("e1 s2 s3 e4", e1, s2, s3, e4)
        e1 = e1 - step
        e1 = round(e1, 3)
    return []


new_A = CutInt(A)
if new_A:
    print("\nВырожденная точечная матрица А': ")
    print_table(CalcMatrix(new_A), headers=[])


