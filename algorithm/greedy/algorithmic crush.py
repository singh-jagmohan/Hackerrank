n, m =map(int,raw_input().split(" "))
lis =[0]*(n+1)
while m :
    m -=1
    a, b, k = map(int,raw_input().split(" "))
    lis[a] += k
    if b+1<=n:
        lis[b] -= k
current = 0
maxi = 0
for i in lis[1:]:
    current += i
    if maxi<current:
        maxi = current
print maxi

