'''
You are given a function f(x) = x^2. You are also given K lists. The i^th list
consists of N_i elements.
You have to pick one element from each list so that the value from the equation
below is maximized:

S = (f(x_1) + f(x_2) + ... + f(x_k)) % M

X_i denotes the element picked from the i^th list . Find the maximized value
S_max obtained.

% denotes the modulo operator.

Note that you need to take exactly one element from each list, not necessarily
the largest element. You add the squares of the chosen elements and perform the
modulo operation. The maximum value that you can obtain, will be the answer to
the problem.

The first line contains 2 space separated integers K and M.
The next K lines each contains an integer N_i, denoting the number of elements
in the i^th list, followed by N_i space separated integers denoting the elements
in the list.
'''

from itertools import product, starmap, takewhile

K,M = map(int,input().split())
K = int(K)
M = int(M)
transform = []
for l in range(K):
    n_array = input().split()
    transform.append(list())
    for x in range(int(n_array[0])):
        transform[l].append(int(n_array[x+1])**2)

S_array = list(product(*transform))
S_max = 0
for t in S_array:
    temp = sum(t)%M #forgot Modulo M
    if temp > S_max:
        S_max = temp
print(S_max)


'''
##################################
# Hrank solution
# above failed 15 of 17 cases
###################################
K,M = map(int,input().split())
N = (list(map(int, input().split()))[1:] for _ in range(K))
results = map(lambda x: sum(i**2 for i in x)%M, product(*N))
print(max(results))
'''
