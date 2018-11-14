#!/bin/python3

from collections import Counter, OrderedDict

class OrderedCounter(Counter, OrderedDict):
    'Counter that remembers the order elements are first encountered'

    def __repr__(self):
        return '%s(%r)' % (self.__class__.__name__, OrderedDict(self))

    def __reduce__(self):
        return self.__class__, (OrderedDict(self),)
# for c in OrderedCounter(sorted(input())).most_common(3):
#     print(*c)
# from collections import Counter


if __name__ == '__main__':
    s = sorted(input())
    c = OrderedCounter(s)
    mos_com = c.most_common(3)
    for i in range(3):
        print(*mos_com[i])
