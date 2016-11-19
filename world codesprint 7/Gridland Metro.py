n, m, k = map(int,raw_input().strip(" ").split(" "))
answer = 0
lis = {}

for i in  range(k):
    r,c1,c2 = map(int,raw_input().strip(" ").split(" "))
    if r-1 not in lis:
        lis[r-1]=[]
    lis[r-1].append([c1,c2])

for subLis in lis:
    total = 0
    newLis = sorted(lis[subLis])
    if len(newLis)!=0:
        start = newLis[0][0]
        end = newLis[0][1]
        total += (end - start) + 1
        for i in newLis[1:]:
            if i[0]<=end:
                if i[1]>end:
                    total += i[1]-end
                    end = i[1]
            else:
                total +=(i[1]-i[0]) + 1
                end = i[1]
    answer +=m - total


print answer+(n-len(lis))*m