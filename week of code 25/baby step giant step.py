import itertools
a = 'AABC'

c =itertools.permutations(a)
for i in c:
    print ''.join(i)


#q =int(raw_input())

# def solve(a,b,d):
#     babyStep = min(a,b)
#     giantStep = max(a,b)
#     steps = 0
#
#     steps += d/giantStep
#     d=d%giantStep
#     if d

# while q:
#     q -=1
#     a,b,d = map(int,raw_input().split())
