from numpy import poly1d

'''
f(x) = x^n + P_1x^(n-1) + ... + P_(n-1)x^1 + P_n

The first line contains the space separated value of the coefficients in P

The second line contains the value of x
'''

P = poly1d(list(map(float,input().split())))
x = float(input())

print(P(x))
