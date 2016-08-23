#!/bin/python

import sys

n, k = raw_input().strip().split(' ')
n, k = [int(n), int(k)]
number = raw_input().strip()
number = list(number)
visited = []
for i in range((n + 1) / 2):
    if number[i] == number[n - 1 - i]:
        pass
    else:
        if number[i] > number[n - i - 1]:
            number[n - i - 1] = number[i]
        else:
            number[i] = number[n - i - 1]
        if number[i] != '9':
            visited.append(i)
        k -= 1
if k < 0:
    print -1
else:
    i = 0
    while k and i < (n + 1) / 2:
        if number[i] != '9':
            if i not in visited:
                if i == n - i - 1:
                    if k > 0:
                        number[i] = '9'
                        k -= 1
                else:
                    if k > 1:
                        number[i] = '9'
                        number[n - i - 1] = '9'
                        k -= 2
            else:
                if k > 0:
                    number[i] = '9'
                    number[n - i - 1] = '9'
                    k -= 1
        i += 1
    print ''.join(number)







