t = int(raw_input())
for i in range(t):
    k,n,b= map(int,raw_input().split(" "))
    val = (n*(n+1))/2-((n-b)*(n-b + 1))/2
    # print "val: ",
    # print val
    start = n-b+1
    minVal=(b*(b+1))/2
    if k<minVal:
        print -1
    elif k>val:
        print -1
    elif n<b:
        print -1
    elif n==b:
        if k == val:
            ans=[]
            for y in range(1,n+1):
                ans.append(str(y))
            print ' '.join(ans)
        else:
            print -1
    else:
        x = val - k
        mini = 1
        ans=[]
        for item in range(start,n+1):
            if x>0:
                if item >x:
                    if item-x>=mini:
                        ans.append(str(item-x))
                        #print item-x,
                        x=0
                    else:
                        x -=item-mini
                        ans.append(str(mini))
                        #print mini,
                        mini +=1
                else:
                    x-=item-mini
                    ans.append(str(mini))
                    #print mini,
                    mini +=1
            else:
                ans.append(str(item))
                #print item,
        print ' '.join(sorted(ans))

