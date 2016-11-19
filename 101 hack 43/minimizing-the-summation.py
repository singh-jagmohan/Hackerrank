#!/bin/python

import sys





global a,currentPosition,k

n,k = raw_input().strip().split(' ')
n,k = [int(n),int(k)]
#a = map(int,raw_input().strip().split(' '))
a = [x for x in xrange(1000)]

table = [[0 for x in range(n)] for y in range(n)]

# for x in range(n):
#     for y in range(n):
#         table[x][y]=abs(a[x]-a[y])**2
# for x in table:
#     print x


result = [[[a[0]],0],[[],0]]

minimumValues=[]
currentPosition=1
indexToBeRemoved=[]
while currentPosition<n:
    newResult = []
    for index,items in enumerate(result):
        #print items
        # sys.exit()
        x = items[0]
        y = items[1]
        newResult.append([x,y])
        # print "res: ",
        # print newResult
        newY = 0
        for item in items[0]:
            newY += items[1]+2*(abs(a[currentPosition]-item)**2)
        newX = items[0]
        newItem = [items[0]+[a[currentPosition]],newY]
        # items[0].append(a[currentPosition])

        #print items
        if len(newItem[0])==k:
            if len(minimumValues)==0:
                minimumValues.append([newItem[0],newItem[1]])
            else:
                if minimumValues[0][1]>newItem[1]:
                    minimumValues[0][1]=newItem[1]
                    minimumValues[0][0]=newItem[0]
        else:
            newResult.append(newItem)
        # print "after: ",
        # print newResult
        # print minimumValues
    # print "sdf",
    # print newResult
    # print "mini",
    # print minimumValues
    result = newResult
    currentPosition +=1

print minimumValues[0][1]

