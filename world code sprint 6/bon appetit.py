# Enter your code here. Read input from STDIN. Print output to STDOUT
n,k=map(int,raw_input().split(" "))
lis=map(int,raw_input().split(" "))
s=int(raw_input())
val=s-(sum(lis)-lis[k])/2
print val if val!=0 else 'Bon Appetit'