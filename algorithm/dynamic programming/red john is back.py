import math
t = int(raw_input())
global fact
fact = {}

def getprimes(P,primes):
    for i in range(2,int(math.sqrt(P))+1):
        if primes[i]==0:
            j = i*2
            while j <=P:
                primes[j]=1
                j += i
    count = 0
    #print primes
    for i in range(2,P+1):
        if primes[i]==0:
            count +=1
    return count







def get_pnc(n,n4,n1):
    if n not in fact:
        fact[n] = math.factorial(n)
    if n4 not in fact:
        fact[n4] = math.factorial(n4)
    if n1 not in fact:
        fact[n1] = math.factorial(n1)

    result = fact[n]/(fact[n4]*fact[n1])
    return result
while t:
    t -=1
    n = int(raw_input())
    P = 0
    for i in range(n/4+1):
        # print "i : ",
        # print i
        P += get_pnc(i+n-(i*4),n-(i*4),i)
    primes = [0]*(P+1)
    #print primes
    if P <2:
        print 0
    else:
        print getprimes(P,primes)