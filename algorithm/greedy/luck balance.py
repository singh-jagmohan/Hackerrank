# Enter your code here. Read input from STDIN. Print output to STDOUT
n, k = map(int, raw_input().split(" "))
lis = []
sumi = 0
while n:
    n -= 1
    luck, important = map(int, raw_input().split(" "))
    if important == 1:
        lis.append(luck)
    else:
        sumi +=luck

lis = sorted(lis)
x=len(lis)
if x <=k:
    print sum(lis)+sumi
else:
    print sum(lis[x-k:])+sumi-sum(lis[:x-k])

