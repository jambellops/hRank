'''

Given a list of numbers and a number k, return whether any two numbers from the
list add up to k.

For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

Bonus: Can you do this in one pass?

'''

def twoaddk(list, k):
    for num in list:
        if k - num in list and k - num != num:
            return True
    return False

# print(twoaddk([10, 15, 3, 7], 17))
#
# print(twoaddk([10, 15, 3, 6], 17))
#
# print(twoaddk([10, 15, 3, 7], 20))
#
# print(twoaddk([10, 15, 5, 7], 20))


'''

Given an array of integers, return a new array such that each element at index i
of the new array is the product of all the numbers in the original array except
the one at i.

For example, if our input was [1, 2, 3, 4, 5], the expected output would be
[120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would be
[2, 3, 6].

Follow-up: what if you can't use division?

'''
from numpy import prod

def allmultexci(array):
    newarray =[]
    for num in array:
        i = array.index(num)
        arraycopy = array[:]
        del arraycopy[i]
        newarray.append(prod(arraycopy))
    return newarray

# print(allmultexci([1, 2, 3, 4, 5]))
# print(allmultexci([3, 2, 1]))
