'''
In this task, we would like for you to appreciate the usefulness of the
groupby() function of itertools . To read more about this function, Check this
out .
You are given a string S. Suppose a character 'c' occurs consecutively X times
in the string. Replace these consecutive occurrences of the character 'c' with
(X,c) in the string.
For a better understanding of the problem, check the explanation.

Input Format
A single line of input consisting of the string S.

Output Format
A single line of output consisting of the modified string.

Constraints
All the characters of S denote integers between 0 and 9.
1<= abs(S) <= 10**4
'''
# From Python 3.7 Docs for itertools.groupby (showing usage):
#
# https://docs.python.org/3.7/library/itertools.html#itertools.groupby
#
# groups = []
# uniquekeys = []
# data = sorted(data, key=keyfunc)
# for k, g in groupby(data, keyfunc):
#     groups.append(list(g))      # Store group iterator as a list
#     uniquekeys.append(k)

from itertools import groupby

S = input()
groups = []
keys = []

for k, g in groupby(S):
    groups.append(list(g))
    keys.append(k)


strout = ''
for i in range(len(keys)):
    tup = (len(groups[i]), int(keys[i]))
    strout += str(tup) + ' '

print(strout)
