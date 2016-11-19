s = raw_input()
lis = []
for index,i in enumerate(s):
    if i == 'a':
        lis.append(index)
t = len(s)
n = int(raw_input())
count = (n/t)*len(lis)
x =  n%t
for i in lis:
    if i<=x-1:
        count +=1
    else:
        break
print count        