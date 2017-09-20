#!/bin/python

import sys

def simpleArraySum(n, ar):
    # Complete this function
    total = 0
    while n > 0:
        total = total + ar[n-1]
        n = n - 1
    return total

n = int(raw_input().strip())
ar = map(int, raw_input().strip().split(' '))
result = simpleArraySum(n, ar)
print(result)
