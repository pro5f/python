#!/bin/python

import sys

def getTotalX(a, b):
    # Complete this function
    count = 0
    n = max(a)
    while max(a)<= n <= min(b):
        if sum(1 for x in a if n%x==0)==len(a) and sum(1 for x in b if x%n==0) == len(b):
            count += 1
            n += 1
        else:
            n += 1
    return count

if __name__ == "__main__":
    n, m = raw_input().strip().split(' ')
    n, m = [int(n), int(m)]
    a = map(int, raw_input().strip().split(' '))
    b = map(int, raw_input().strip().split(' '))
    total = getTotalX(a, b)
    print total