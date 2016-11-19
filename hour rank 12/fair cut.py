n , k = map(int,raw_input().split(" "))
lis = map(int,raw_input().split(" "))
lis = sorted(lis)
start = 0
end = n -1
term = 0
new = []
for i in range(n-k-1):
    if term:
        new.append(start)
        start +=1
        term ^=1
    else:
        new.append(end)
        term ^= 1
        end -=1
val1 = 0
val2 = 0
for j in range(start+1,end+1):
    val1 +=abs(lis[start]-lis[i])
for j in range(start,end):
    val2 +=abs(lis[end]-lis[i])
if val1<val2:
    new.append(start)
else:
    new.append(end)
new2 = []
for i in range(n):
    if i not in new:
        new2.append(i)

sumi = 0

#
# print new
# print new2
for k in new:
    for l in new2:
        sumi +=abs(lis[k]-lis[l])
print sumi





