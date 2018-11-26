'''
itertools.combinations(iterable, r)
This tool returns the  length subsequences of elements from the input iterable.
Combinations are emitted in lexicographic sorted order. So, if the input iterable is sorted, the combination tuples will be produced in sorted order.

Sample Code
>>> from itertools import combinations
>>>
>>> print list(combinations('12345',2))
[('1', '2'), ('1', '3'), ('1', '4'), ('1', '5'), ('2', '3'), ('2', '4'), ('2', '5'), ('3', '4'), ('3', '5'), ('4', '5')]
>>>
>>> A = [1,1,3,3,3]
>>> print list(combinations(A,4))
[(1, 1, 3, 3), (1, 1, 3, 3), (1, 1, 3, 3), (1, 3, 3, 3), (1, 3, 3, 3)]

Task
You are given a string S.
Your task is to print all possible combinations, up to size k, of the string in lexicographic sorted order.
Input Format
A single line containing the string S and integer value k separated by a space.
Constraints
0 < k <= len(S)
The string contains only UPPERCASE characters.

Output Format
Print the different combinations of string  on separate lines.
Sample Input
HACK 2

Sample Output
A
C
H
K
AC
AH
AK
CH
CK
HK

'''

# this version accounts for getting a combination of each value
# up to k
# from itertools import combinations_with_replacement
#
# S, k = input().split()
# S = sorted(S)
# k = int(k)
# #
# # for l in range(1, k+1):
# #     listout = list(combinations(S,l))
# #     for i in range(len(listout)):
# #         comb_i = listout[i]
# #         strout = ''
# #         for j in range(len(comb_i)):
# #             strout += comb_i[j]
# #         print(strout)
#
# listout = list(permutations(sorted(S),k))
# for c in S:
#     print(c)
# for i in range(len(listout)):
#     comb_i = listout[i]
#     strout = ''
#     for j in range(len(comb_i)):
#         strout += comb_i[j]
#     print(strout)
from itertools import combinations_with_replacement

S, k = input().split()
S = sorted(S)
k = int(k)

listout = list(combinations_with_replacement(S,k))
for i in range(len(listout)):
    comb_i = listout[i]
    strout = ''
    for j in range(len(comb_i)):
        strout += comb_i[j]
    print(strout)
