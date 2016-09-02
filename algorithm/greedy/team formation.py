t = int(raw_input())
while t:
    t -=1
    lis = map(int,raw_input().split(" "))


    n = lis[0]
    if n!=0:
        lis = lis[1:]
        newLis = sorted(lis)
        mini = 1
        while 1:
            flag = 0
            size = 1
            start = newLis[0]
            duplicates = []
            for index,i in enumerate(newLis[1:]):
                if i-start==1:
                    # print "there"
                    size +=1
                    if index == n - 2:
                        if flag == 0:
                            mini = size
                            flag = 1
                        if mini > size:
                            # print "x"
                            mini = size
                elif i-start==0:
                    duplicates.append(i)
                else:
                    #print "here"
                    if flag==0:
                        mini = size
                        flag = 1
                    if mini>size:
                        mini = size
                    size = 1
                    if index == n-2:
                        mini = 1
                start = i
            if len(duplicates)==0:
                break
            else:
                newLis = duplicates
                print newLis
                print mini
                print size


        print mini
    else:
        print 0