'''
Task
You have a non-empty set s, and you have to execute N commands given in N lines.
The commands will be pop, remove and discard.

Input Format
The first line contains integer n, the number of elements in the set .
The second line contains n space separated elements of set s. All of the
elements are non-negative integers, less than or equal to 9.
The third line contains integer N, the number of commands.
The next N lines contains either pop, remove and/or discard commands followed
by their associated value.

'''
n = int(input()) # size of s
s = set(map(int, input().split()))
N = int(input()) # number of commands
for i in range(N):
    line = input().split(maxsplit=-1)
    if len(line)>1:
        action = line[0]
        value = int(line[1])
        getattr(s, action)(value)
    else:
        action = line[0]
        getattr(s, action)()

print(sum(s))
