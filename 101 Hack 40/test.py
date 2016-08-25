from operator import itemgetter
import sys
n, q = map(int, raw_input().split(" "))
dic = {}
for i in range(n):
    x1, y1, x2, y2 = map(float, raw_input().split(" "))
    if x1 > x2:
        for i in range(int(x2),int(x1)+1):
            if i not in dic:
                dic[i] = []
            # print y2-y1
            # print x2-x1
            # print i-x1
            val = ((y2-y1)/(x2-x1))*(i-x1)+y1
            if y1>y2:
                dic[i].append([val,x2])
            else:
                dic[i].append([val,x1])
    else:
        for i in range(int(x1),int(x2)+1):
            if i not in dic:
                dic[i] = []
            val = ((y2-y1)/(x2-x1))*(i-x1)+y1
            if y1>y2:
                dic[i].append([val,x2])
            else:
                dic[i].append([val,x1])

#print dic
for j in range(q):
    x, y = map(int, raw_input().split(" "))
    if x not in dic:
        print x
    while True:
        #print sorted(dic[x], key=itemgetter(1))
        y = int(sorted(dic[x], key=itemgetter(1))[0][1])
        if x==y:
            break
        if x not in dic:
            break
        x = y
        # print x
        # sys.exit()


    print x

