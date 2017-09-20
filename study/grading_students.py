#!/bin/python

import sys

def solve(grades):
    # Complete this function
    out = []
    for k in grades:
        if int(k) <38:
        	out.append(int(k))
        elif (5 - (int(k) % 5)) < 3:
        	out.append(str(int(k)+ (5-(int(k)%5))))
        else:
        	out.append(str(k))
    return out       

n = int(raw_input().strip())
grades = []
grades_i = 0
for grades_i in xrange(n):
    grades_t = int(raw_input().strip())
    grades.append(grades_t)
result = solve(grades)
print "\n".join(map(str, result))
