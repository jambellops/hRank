from itertools import product

A = input().split()
for i in range(len(A)):
    A[i] = int(A[i])
B = input().split()
for i in range(len(B)):
    B[i] = int(B[i])

AxB = product(A,B)
print(*AxB)
