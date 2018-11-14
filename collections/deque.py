'''
Task
Perform append, pop, popleft and appendleft methods on an empty deque d.

Input Format
The first line contains an integer N, the number of operations.
The next N lines contains the space separated names of methods and their values.

Constraints
0< N <= 100

Output Format
Print the space separated elements of deque d.
'''

from collections import deque

d = deque()
N = int(input())

for i in range(N):

    line = input().split(maxsplit=-1)
    if len(line)>1:
        action = line[0]
        value = line[1]
        getattr(d, action)(value)
    else:
        action = line[0]
        getattr(d, action)()

print(*d)
