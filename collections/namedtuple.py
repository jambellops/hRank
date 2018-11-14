'''
The first line contains an integer N, the total number of students.
The second line contains the names of the columns in any order.
The next N lines contains the Marks, IDs, name and class, under their respective
 column names.

 >>> from collections import namedtuple
>>> Point = namedtuple('Point','x,y')
>>> pt1 = Point(1,2)
>>> pt2 = Point(3,4)
>>> dot_product = ( pt1.x * pt2.x ) +( pt1.y * pt2.y )
>>> print dot_product
11

>>> from collections import namedtuple
>>> Car = namedtuple('Car','Price Mileage Colour Class')
>>> xyz = Car(Price = 100000, Mileage = 30, Colour = 'Cyan', Class = 'Y')
>>> print xyz
Car(Price=100000, Mileage=30, Colour='Cyan', Class='Y')
>>> print xyz.Class
Y

Note:
1. Columns can be in any order. IDs, marks, class and name can be written in any
 order in the spreadsheet.
2. Column names are ID, MARKS, CLASS and NAME. (The spelling and case type of
 these names won't change.)
'''
'''
from collections import namedtuple
#
# if __name__ == '__main__':
#     # Number of student
N = int(input())
grade = namedtuple('grade', input())
students = []
for i in range(N)
    grade(input())
'''

from collections import namedtuple
N, headers = (int(input()), input().split())
grade = namedtuple('grade', headers)
if N > 0:
    student_avg = sum([int(grade._make(input().split()).MARKS) for _ in range(N)])/N
    print(format(student_avg,'.2f'))
else:
    print(0)
