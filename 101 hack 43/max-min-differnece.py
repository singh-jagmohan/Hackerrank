n = int(raw_input())
lis=map(int,raw_input().split(" "))
lis =sorted(lis)
print min(lis[-1]-lis[1],lis[-2]-lis[0])