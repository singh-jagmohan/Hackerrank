# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(raw_input())
a=[]
for i in range(n):
    a.append(sum(sorted(map(int,raw_input().split(' ')))[1:]))
print max(a)
