'''
There is a horizontal row of n cubes. The length of each cube is given. You need
 to create a new vertical pile of cubes. The new pile should follow these
 directions: if cube_i is on top of cube_j then sidelength_i <= sidelength_j.
When stacking the cubes, you can only pick up either the leftmost or the
 rightmost cube each time. Print "Yes" if it is possible to stack the cubes.
 Otherwise, print "No". Do not print the quotation marks.

Input Format
The first line contains a single integer T, the number of test cases.
For each test case, there are 2 lines.
The first line of each test case contains n, the number of cubes.
The second line contains n space separated integers, denoting the sideLengths of
 each cube in that order.

Constraints
 1 <= T <= 5
 1 <= n <= 10^5
 1 <= sidelength <= 2^31

Output Format
For each test case, output a single line containing either "Yes" or "No" without
 the quotes.

Sample Input
2
6
4 3 2 1 3 4
3
1 3 2

Sample Output
Yes
No

Explanation
In the first test case, pick in this order: left - 4, right - 4, left - 3,
 right - 3, left - 2, right - 1.
In the second test case, no order gives an appropriate arrangement of vertical
 cubes. 3 will always come after either 1 or 2.

a helper function might be useful for recursion
'''

'''
some Psudo cod:



for each in T
    from input eval next n input int()s

        from input_split is input_split[0 or -1] >= each of remaining input_split[:]

        recursive:
        if input_split[0] < any of input_split

'''
from collections import deque

T = int(input())
for case in range(T):
    message = "Yes"
    n = int(input())
    d = deque(map(int, input().strip().split()))
    for max_side in reversed(sorted(d)):
        if d[0]!=max_side and d[-1]!=max_side:
            message="No"
            break;
        elif d[0]==max_side:
            d.popleft()
        else:
            d.pop()
    print(message)
