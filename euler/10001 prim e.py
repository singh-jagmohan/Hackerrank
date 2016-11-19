#!/bin/python

import sys


t = int(raw_input().strip())
for a0 in xrange(t):
    n = int(raw_input().strip())
    noprimes = [j for i in range(2, int(pow(100000,0.5))+1) for j in range(i*2, 100000, i)]
    primes = [x for x in range(2, 100000) if x not in noprimes]
    print len(primes)
