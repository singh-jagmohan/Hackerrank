import math
n,m = map(int,raw_input().lstrip().rstrip().split(" "))
count = 0
angle = 0
pos = 0
#n=float(n)
minAngle = 360/(2*n)
#print minAngle
while m:
    m -=1
    a,b = map(int,raw_input().split(" "))
    if a ==1:
        #angle += 2*b
        pos +=b
        # if count%2==0:
        #     pass
        # else:
        #     angle -= minAngle * 2 * b
    else:
        if count%2==0:
            pos += b
        else:
            pos -= b
        count +=1
    #print pos
#     print angle
# print angle
# print count
# pos= -8
# n = 5
if pos <0:
    pos = -(abs(pos)%n)
    pos = n+pos
else:
    pos = pos % n
#print pos
#angle=(minAngle*angle)%360
# if angle<0:
#     angle=360+angle
print pos
if count%2==0:
    print 1,n-pos
    #print 1,int(math.ceil((360-angle)/(2*minAngle)))
else:
    print 2,n-pos
    #print 2, int(math.ceil((angle/2)/(minAngle)))
