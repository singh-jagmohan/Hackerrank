n = int(raw_input())
sides =map(int,raw_input().split(" "))
sides =sorted(sides,reverse=True)

flag = 0
for i in range(n):
    for j in range(i+1,n):
        for k in range(i+2,n):
            if sides[k]+sides[j]>sides[i]:
                print sides[k],sides[j],sides[i]
                flag = 1
                break
        if flag==1: break
    if flag==1:break

if flag==0:    print -1