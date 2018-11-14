'''
You are given a string S.
Your task is to find out whether S is a valid regex or not.

Input Format
The first line contains integer T, the number of test cases.
The next T lines contains the string S.

Constraints

0 < T < 100

Output Format
Print "True" or "False" for each test case without quotes.
'''
import re

T = int(input())
for i in range(T): # other submitters directly looped over the input
    S = input() # other submitters directly compiled the input
    try:
        print(bool(re.compile(S))) #if it compiles it's True
    except: #need to handle the exception on re.compile
        print('False')
