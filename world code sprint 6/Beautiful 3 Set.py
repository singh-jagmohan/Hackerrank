import operator, sys
n=int(raw_input())
lis=[]
for i in range(n+1):
    for j in range(n+1):
        for k in range(n+1):
            if i+j+k==n:

                flag=0
                for index,item in enumerate(lis):
                    if i not in item[1] and j not in item[2] and k not in item[3]:
                        item[1].add(i)
                        item[2].add(j)
                        item[3].add(k)
                        lis[index][0].append([i,j,k])
                        lis[index][4] += 1
                        flag = 1
                    if j not in item[1] and k not in item[2] and i not in item[3]:
                        item[1].add(j)
                        item[2].add(k)
                        item[3].add(i)
                        lis[index][0].append([j,k,i])
                        lis[index][4] += 1
                        flag = 1
                    if k not in item[1] and i not in item[2] and j not in item[3]:
                        item[1].add(k)
                        item[2].add(i)
                        item[3].add(j)
                        lis[index][0].append([k,i,j])
                        lis[index][4] += 1
                        flag =1

                if flag==0:
                    if i != j and j != k and i != k:
                        lis.append([[[i, j, k]], set([i]), set([j]), set([k]), 1])
                        lis.append([[[k, i, j]], set([k]), set([i]), set([j]), 1])
                        lis.append([[[j, k, i]], set([j]), set([k]), set([i]), 1])
                    else:
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





# n = int(raw_input())
# if n<3:
#     if n==2:
#         print 1
#         print "0 1 1"
#     if n==1:
#         print 1
#         print "0 0 1"
# else:
#     visitedx={}
#     visitedy={}
#     visitedz={}
#     single=[]
#     result=[]
#     lis=[item for item in range(n)]
#     x=lis[0]
#     y=lis[1]
#     z=lis[-1]
#     result.append([x,y,z])
#     visitedx[x]=1
#     visitedy[y]=1
#     visitedz[z]=1
#     while 1:
#         x=y+1
#         y=y+2
#         z=z-4
#         if z>y:
#             result.append([x,y,z])
#         else:
#             y-=1
#             z=n-x-y
#             if z>=x:
#                 single.append([x,y,z])
#             break
#     print 3*len(result)+len(single)
#     # item = result[-1]
#     # x = item[0]
#     # y = item[1]
#     # z = item[2]
#     # print x, y, z
#     # print z, x, y
#     # print y, z, x
#     for item in result:
#         x=item[0]
#         y=item[1]
#         z=item[2]
#         print x,y,z
#         print z,x,y
#         print y,z,x
#     for item in single:
#         x = item[0]
#         y = item[1]
#         z = item[2]
#         print x, y, z