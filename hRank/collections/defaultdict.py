'''
The first line contains integers, n and m separated by a space.
The next n lines contains the words belonging to group A.
The next m lines contains the words belonging to group B.

Output m lines.
The "i"th line should contain the 1-indexed positions of the occurrences of the
 "i"th word separated by spaces.
'''
from collections import defaultdict
a = defaultdict(list)
n, m = input().split()
for i in range(int(n)):
    a[input()].append(i + 1)

for i in range(int(m)):
    for j in a.get(input(), [-1]):
        print(j, end = " ")
    print()
