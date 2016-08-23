#!/bin/python

import sys

n = int(raw_input().strip())
for a0 in xrange(n):
    S = raw_input().strip()
    # print S
    # sys.exit()
    A = [0] * 26
    count = 0
    for i in range(len(S)):
        A[ord(S[i]) - ord('a')] += 1
    for i in A:
        if i > 0:
            count += 1
    print count

