#!/bin/python

import sys


s = raw_input().strip()
t = raw_input().strip()
k = int(raw_input().strip())
lenT =len(t)
for i in range(len(s)):
    if i<lenT:
        if s[i]==t[i]:
            pass
        else:
            break
    else:
        break



matchedCharacter = i
remainingS = len(s)-matchedCharacter
remainingT = len(t)-matchedCharacter
remainingK = k-(remainingS+remainingT)
# print matchedCharacter
# print remainingS
# print remainingK
# print remainingT
if k >=len(s)+lenT:
    print "Yes"

else:
    if remainingK>=0:
        if remainingK%2==0:
            print "Yes"
        elif remainingK/2>=lenT:
            print "Yes"
        else:
            print "No"
    else:
        print "No"
