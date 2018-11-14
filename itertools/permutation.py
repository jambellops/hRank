'''
Task
You are given a string S.
Your task is to print all possible permutations of size k of the string in lexicographic sorted order.

Input Format
A single line containing the space separated string S and the integer value k.

Constraints
0 < k <= len(S)
The string contains only UPPERCASE characters.

Output Format
Print the permutations of the string S on separate lines.
'''

from itertools import permutations

S, k = input().split()

k = int(k)
listout = list(permutations(sorted(S),k))

for i in range(len(listout)):
    comb_i = listout[i]
    strout = ''
    for j in range(len(comb_i)):
        strout += comb_i[j]
    print(strout)
