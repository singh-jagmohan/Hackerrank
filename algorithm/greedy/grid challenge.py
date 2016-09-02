# Enter your code here. Read input from STDIN. Print output to STDOUT
t = int(raw_input())
def check(s1,s2,n):
    for i in range(n):
        if s1[i]<=s2[i]:
            pass
        else:
            return False
    return True
while t:
    t -= 1
    n = int(raw_input())
    lis = []
    while n:
        n-=1
        lis.append(raw_input())
    a =  sorted(lis[0])
    x=len(a)
    flag=0
    for index,i in enumerate(lis[1:]):
        b = sorted(i)
        if check(a,b,x):
            a=b
            pass
        else:
            flag=1
            print "NO"
            break
    if flag ==0:
        print "YES"