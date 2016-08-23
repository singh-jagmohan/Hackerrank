#!/bin/python

import sys

n = int(raw_input().strip())
a = map(int, raw_input().strip().split(' '))
maxi = max(a)
sumi = sum(a)
if n == 2:
    if a[0] == a[1]:
        print 2
    else:
        print 1
elif n == 1:
    print 2
else:
    if sumi - maxi > maxi:
        print 0
    else:
        print 1

