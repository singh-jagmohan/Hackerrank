#!/bin/python

import sys

n, m = raw_input().strip().split(' ')
n, m = [int(n), int(m)]
if n >= m:
    print n - m
else:
    if m % n == 0:
        print 0
    else:

        print n - (m % n)