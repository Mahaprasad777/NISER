#Name-Mahaprasad Manoranjan Sahoo, Roll No-2311096
from mahalib import mylib

#Question-1
n=mylib()
A = []
with open("matrixA.txt", "r") as f:
    for line in f:
        row = list(map(float, line.split()))
        A.append(row)

b = []
with open("matrixB.txt", "r") as f:
    for line in f:
        b.extend(list(map(float, line.split())))

print("Matrix A:")
for row in A:
    print(row)
print("\nVector b:", b)

L = n.cholesky_decom(A)
x = n.cholesky_sol(L, b)
print("\nSolution after using Cholesky Decomposition Method:", x)
print('\n')

#Solution:
'''
Matrix A:
[4.0, 1.0, 1.0, 1.0]
[1.0, 3.0, -1.0, 1.0]
[1.0, -1.0, 2.0, 0.0]
[1.0, 1.0, 0.0, 2.0]

Vector b: [3.0, 3.0, 1.0, 3.0]

Solution after using Cholesky Decomposition Method: [-5.551115123125783e-17, 0.9999999999999999, 1.0, 1.0000000000000002]
'''

#Question-2


A = []
with open("matrixA.txt", "r") as f:
    for line in f:
        row = list(map(float, line.split()))
        A.append(row)


b = []
with open("matrixB.txt", "r") as f:
    for line in f:
        b.extend(list(map(float, line.split())))

print("Matrix A:")
for row in A:
    print(row)
print("\nVector b:", b)
m=n.jacobi_sol(A, b,tol=1e-6)
print("\nSolution after using Jacobi Iterative Method:", m)
print("The Number present at the last is the No of iterations!!")

#Solution:
'''
Matrix A:
[4.0, 1.0, 1.0, 1.0]
[1.0, 3.0, -1.0, 1.0]
[1.0, -1.0, 2.0, 0.0]
[1.0, 1.0, 0.0, 2.0]

Vector b: [3.0, 3.0, 1.0, 3.0]

Solution after using Jacobi Iterative Method: ([0.0, 0.9999994039535522, 0.9999997019767761, 0.9999997019767761], 42)
The Number present at the last is the No of iterations!!'''