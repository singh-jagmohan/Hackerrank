# Enter your code here. Read input from STDIN. Print output to STDOUT
t = int(raw_input())
lis1 = map(int, raw_input().split(' '))
lis2 = map(int, raw_input().split(' '))
if sum(lis1) != sum(lis2):
    print -1
else:
    count = 0
    lis1 = sorted(lis1)
    lis2 = sorted(lis2)
    for i in range(t):
        if lis1[i] == lis2[i]:
            pass
        else:
            if lis1[i] > lis2[i]:
                count += lis1[i] - lis2[i]
    print count
