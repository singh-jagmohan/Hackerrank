#!/bin/python

import sys


S = raw_input().strip()
l = len(S)
count = 0
for i in range(0,l,3):
    if S[i] != 'S':
        count += 1
    if S[i+1] != 'O':
        count += 1
    if S[i+2] != 'S':
        count += 1
print count
