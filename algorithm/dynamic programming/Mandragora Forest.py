t = int(raw_input())
while t:
    t -= 1
    n = int(raw_input())
    array = map(int, raw_input().split(" "))
    P = 0
    S = n
    array = sorted(array)
    P = array[n-1]
    for i in range(n-2,0,-1):
        PNew = S*P
        POld = array[i]*(S-1)+(S-1)*P
        if PNew>=POld:
            break
        else:
            P += array[i]
            S -=1
    print P*S


