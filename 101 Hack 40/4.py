import sys
n, q = map(int, raw_input().split(" "))
dic = {}
for k in range(n):
    x1, y1, x2, y2 = map(float, raw_input().split(" "))
    if x1 > x2:
        for i in range(int(x2), int(x1) + 1):
            print "first: ",
            print i
            if i not in dic:
                dic[i] = []
            dic[i].append([x1, y1, x2, y2])
    else:
        for i in range(int(x1), int(x2) + 1):
            print "second: ",
            print i
            if i not in dic:
                dic[i] = []
            dic[i].append([x1, y1, x2, y2])

for j in range(q):
    x, y = map(int, raw_input().split(" "))
    if x not in dic:
        print x
    else:
        while True:
            check = 0
            for i in dic[x]:
                #print i
                x1 = i[0]
                y1 = i[1]
                x2 = i[2]
                y2 = i[3]

                newY = ((y2 - y1) / (x2 - x1)) * (x - x1) + y1
                #print newY
                if y >= newY:
                    if check == 0:
                        check += 1
                        val = newY
                        if y1 > y2:
                            #print "1"
                            newX = x2
                            tempY = y2
                            # print newX
                            # print tempY
                        else:
                            #print "2"
                            newX = x1
                            tempY = y1
                            # print newX
                            # print tempY
                    else:

                        #print "3"
                        if val < newY:

                            val = newY
                            if y1 > y2:
                                #print "4"
                                newX = x2
                                tempY = y2
                                # print newX
                                # print tempY
                            else:
                                #print "5"
                                newX = x1
                                tempY = y1
                                # print newX
                                # print tempY

            if (x==int(newX) and y== int(tempY)) or x not in dic:
                print x
                break
            x = int(newX)
            y = int(tempY)


