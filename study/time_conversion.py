#!/bin/python

import sys, re

def timeConversion(s):
    # Complete this function
    out = []
    if re.match(r"(\d+:\d+:\d+)(PM)", s):
        k  = re.match(r"(\d+):(\d+:)(\d+)(PM)", s)
        out=(str(int(k.group(1))%12+12))+":"+k.group(2)+k.group(3)
        return out
    else:
        k  = re.match(r"(\d+)(:\d+:\d+)(AM)", s)
        if int(k.group(1)) == 12:
            out = "00"+k.group(2)
        else:
            out = k.group(1)+k.group(2)
        return out

s = raw_input().strip()
result = timeConversion(s)
print(result)

