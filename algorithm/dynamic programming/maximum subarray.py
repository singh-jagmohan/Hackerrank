t = int(raw_input())
while t:
    t -= 1
    n = int(raw_input())
    lis = map(int,raw_input().split(" "))
    subSequenceArraySum =lis[0]
    maxi= lis[0]
    sumi = lis[0]
    flag = 0
    i = 1
    while i < n:
        if lis[i]<0:
            if sumi + lis[i]< lis[i]:
                sumi = lis[i]
                if maxi<sumi:
                    maxi = lis[i]
            elif sumi + lis[i]<sumi:
                if maxi<sumi:
                    maxi = sumi
                if sumi+lis[i]<0:
                    if sumi + lis[i]<lis[i]:
                        sumi = lis[i]
                    else:
                        sumi +=lis[i]
                else:
                    sumi +=lis[i]
        else:
            flag = 1
            if sumi<0:
                sumi = lis[i]
            else:
                sumi +=lis[i]
            if maxi<sumi:
                maxi = sumi
            if subSequenceArraySum<0:
                subSequenceArraySum = lis[i]
            else:
                subSequenceArraySum +=lis[i]
        i += 1
    if flag == 0:
        print maxi,maxi
    else:
        print maxi,subSequenceArraySum
