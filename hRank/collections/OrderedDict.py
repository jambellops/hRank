'''
>>> ordered_dictionary = OrderedDict()
>>> ordered_dictionary['a'] = 1
>>> ordered_dictionary['b'] = 2
>>> ordered_dictionary['c'] = 3
>>> ordered_dictionary['d'] = 4
>>> ordered_dictionary['e'] = 5
'''

'''
Task
You are the manager of a supermarket.
You have a list of N items together with their prices that consumers bought on a particular day.
Your task is to print each item_name and net_price in order of its first occurrence.
item_name = Name of the item.
net_price = Quantity of the item sold multiplied by the price of each item.

Input Format
The first line contains the number of items, N.
The next N lines contains the item's name and price, separated by a space.

Constraints
0<= N <= 100

Output Format
Print the item_name and net_price in order of its first occurrence.
'''
from collections import OrderedDict

N = int(input())
transact_dict = OrderedDict()
for t in range(N):
    item,price = input().rsplit(maxsplit = 1)
    if item in transact_dict:
        transact_dict[item] += int(price)
    else:
        transact_dict[item] = int(price)

for item in transact_dict:
    print(item + ' ' + str(transact_dict[item]))
