'''
The itertools module standardizes a core set of fast, memory efficient tools
that are useful by themselves or in combination. Together, they form an iterator
algebra making it possible to construct specialized tools succinctly and
efficiently in pure Python.

To read more about the functions in this module, check out their documentation
here.
Task
You are given a list of N lowercase English letters. For a given integer K, you
can select any K indices (assume 1-based indexing) with a uniform probability
from the list.
Find the probability that at least one of the K indices selected will contain
the letter: 'a'.

Input Format
The input consists of three lines. The first line contains the integer N,
denoting the length of the list. The next line consists of N space-separated
lowercase English letters, denoting the elements of the list.
The third and the last line of input contains the integer K, denoting the number
of indices to be selected.

Output Format
Output a single line consisting of the probability that at least one of the K
indices selected contains the letter:'a'.

Note: The answer must be correct up to 3 decimal places.
Constraints
1 <= N <= 10
1 <= K <= N

All the letters in the list are lowercase English letters.
'''
from itertools import combinations

N = int(input())
n_list = input().split()
K = int(input())

listout = list(combinations(n_list,K))


a_is_in = 0

for j in range(len(listout)):
    if 'a' in listout[j]:
        a_is_in +=1
print(float(a_is_in/len(listout)))
'''
# import itertools
#
# N = int(input())
# n_list = input().split()
# K = int(input())
#
# #create possible slices
# iter_array = []
# a_is_in = 0
# for i in range(N-K):
#     looplist = list(islice(n_list, i, i + K), sep=' ')
#     print(looplist)
#     iter_array.append(looplist)
# print(iter_array)
# for j in range(N-K):
#     if 'a' in iter_array[j]:
#         a_is_in +=1
# print(float(a_is_in/len(iter_array))
'''    
