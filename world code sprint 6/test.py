import operator, sys, datetime
n=int(raw_input())
lis=[]
xList={}
yList ={}
zList = {}
listIndex=0
start = datetime.datetime.now()
for i in range(n+1):
    for j in range(n+1):
        for k in range(n+1):
            if i+j+k==n:

                flag=0
                totalIndex=[p for p in range(listIndex)]
                if i not in xList:
                    xList[i] = []
                if j not in yList:
                    yList[j] = []
                if k not in zList:
                    zList[k] = []

                if k not in xList:
                    xList[k] = []
                if i not in yList:
                    yList[i] = []
                if j not in zList:
                    zList[j] = []

                if j not in xList:
                    xList[j] = []
                if k not in yList:
                    yList[k] = []
                if i not in zList:
                    zList[i] = []
                ind1=list(set(totalIndex)-set(xList[i])-set(yList[j])-set(zList[k]))
                ind2=list(set(totalIndex)-set(xList[k])-set(yList[i])-set(zList[j]))
                ind3=list(set(totalIndex)-set(xList[j])-set(yList[k])-set(zList[i]))
                for d in range(len(ind1)):
                    index=d
                    item=lis[index]
                    if i not in item[1] and j not in item[2] and k not in item[3]:
                        item[1].add(i)
                        item[2].add(j)
                        item[3].add(k)
                        lis[index][0].append([i, j, k])
                        lis[index][4] += 1
                        flag = 1

                        xList[i].append(index)
                        yList[j].append(index)
                        zList[k].append(index)
                for e in range(len(ind2)):
                    index = e
                    item = lis[index]
                    if j not in item[1] and k not in item[2] and i not in item[3]:
                        item[1].add(j)
                        item[2].add(k)
                        item[3].add(i)
                        lis[index][0].append([j, k, i])
                        lis[index][4] += 1
                        flag = 1

                        xList[k].append(index)
                        yList[i].append(index)
                        zList[j].append(index)
                for f in range(len(ind3)):
                    index = f
                    item = lis[index]
                    if k not in item[1] and i not in item[2] and j not in item[3]:
                        item[1].add(k)
                        item[2].add(i)
                        item[3].add(j)
                        lis[index][0].append([k, i, j])
                        lis[index][4] += 1
                        flag = 1

                        xList[j].append(index)
                        yList[k].append(index)
                        zList[i].append(index)


                # ## skip xlist ylist and zlist combined
                # for index,item in enumerate(lis):
                #     if i not in item[1] and j not in item[2] and k not in item[3]:
                #         item[1].add(i)
                #         item[2].add(j)
                #         item[3].add(k)
                #         lis[index][0].append([i,j,k])
                #         lis[index][4] += 1
                #         flag = 1
                #
                #         xList[i].append(index)
                #         yList[j].append(index)
                #         zList[k].append(index)
                #     if j not in item[1] and k not in item[2] and i not in item[3]:
                #         item[1].add(j)
                #         item[2].add(k)
                #         item[3].add(i)
                #         lis[index][0].append([j,k,i])
                #         lis[index][4] += 1
                #         flag = 1
                #
                #         xList[k].append(index)
                #         yList[i].append(index)
                #         zList[j].append(index)
                #     if k not in item[1] and i not in item[2] and j not in item[3]:
                #         item[1].add(k)
                #         item[2].add(i)
                #         item[3].add(j)
                #         lis[index][0].append([k,i,j])
                #         lis[index][4] += 1
                #         flag =1
                #
                #         xList[j].append(index)
                #         yList[k].append(index)
                #         zList[i].append(index)

                if flag==0:
                    if i != j and j != k and i != k:
                        if i not in xList:
                            xList[i]=[]
                        if j not in yList:
                            yList[j]=[]
                        if k not in zList:
                            zList[k]=[]
                        xList[i].append(listIndex)
                        yList[j].append(listIndex)
                        zList[k].append(listIndex)
                        listIndex += 1
                        lis.append([[[i, j, k]], set([i]), set([j]), set([k]), 1])
                        if k not in xList:
                            xList[k]=[]
                        if i not in yList:
                            yList[i]=[]
                        if j not in zList:
                            zList[j]=[]
                        xList[k].append(listIndex)
                        yList[i].append(listIndex)
                        zList[j].append(listIndex)
                        listIndex += 1
                        lis.append([[[k, i, j]], set([k]), set([i]), set([j]), 1])
                        if j not in xList:
                            xList[j]=[]
                        if k not in yList:
                            yList[k]=[]
                        if i not in zList:
                            zList[i]=[]
                        xList[j].append(listIndex)
                        yList[k].append(listIndex)
                        zList[i].append(listIndex)
                        listIndex += 1
                        lis.append([[[j, k, i]], set([j]), set([k]), set([i]), 1])
                    else:
                        if i not in xList:
                            xList[i]=[]
                        if j not in yList:
                            yList[j]=[]
                        if k not in zList:
                            zList[k]=[]
                        xList[i].append(listIndex)
                        yList[j].append(listIndex)
                        zList[k].append(listIndex)
                        listIndex += 1
                        lis.append([[[i, j, k]], set([i]), set([j]), set([k]), 1])

                # else:
                #     lis.append([[[i, j, k]], set([i]), set([j]), set([k]), 1])

# for x in lis:
#     print x[0],x[4]
# sys.exit()
newLis=[item[4] for item in lis]
index, value = max(enumerate(newLis), key=operator.itemgetter(1))
#print index
# print lis[index][1]
print lis[index][4]
for item in lis[index][0]:
    print item[0],item[1],item[2]
# for item in newLis:
#     print item

print datetime.datetime.now() -start