#!/bin/python

import sys


def kangaroo(x1, v1, x2, v2):
    # Complete this function
    count = 0
    if (v1 == v2):
        return "NO"
    elif (v2 < v1) and ((x2 - x1) % (v1 - v2) == 0):
        return "YES"
    else:
        return "NO"


x1, v1, x2, v2 = raw_input().strip().split(' ')
x1, v1, x2, v2 = [int(x1), int(v1), int(x2), int(v2)]
result = kangaroo(x1, v1, x2, v2)
print(result)
