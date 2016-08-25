import sys,datetime
global OPERATION
n, m = map(int, raw_input().split(' '))
OPERATION=[]
def checkSubset(tobechecked,checkwith):
    for i in range(n):
        if checkwith[i]=='0':

            if tobechecked[i]=='1':
                return False
    return True


def add(x,S):
    OPERATION.append([1,x,S])


def xor(x,S):
    OPERATION.append([2,x,S])


def print_func(S):
    val=0
    check=0
    xor=0
    for i in OPERATION[::-1]:
        if checkSubset(S,i[2]):
            if i[0]==1:
                val=i[1]
                break
            else:
                xor ^= i[1]
                check=1
                
    if check==1:
        print val^xor
    else:
        print val
for i in range(m):
    query = raw_input().split(' ')
    if query[0] == '1':
        x = int(query[1])
        S = query[2]
        add(x,S)

    elif query[0] == '2':
        x = int(query[1])
        S = query[2]
        xor(x,S)

    else:
        S = query[1]
        print_func(S)
