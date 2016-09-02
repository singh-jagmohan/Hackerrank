import math
import datetime
def getprimes(P):
    primes = [0]*(P+1)
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
