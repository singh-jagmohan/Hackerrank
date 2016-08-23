#!/usr/bin/py
def lonelyinteger(a):
    n=[0]*100
    for i in a:
        n[i]+=1
    #print n
    for i in range(100):
        if n[i]==1:
            return i
    answer = 0
    return answer
if __name__ == '__main__':
    a = input()
    b = map(int, raw_input().strip().split(" "))
    print lonelyinteger(b)
