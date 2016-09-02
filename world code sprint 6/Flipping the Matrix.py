t = int(raw_input())
while t:
    t -= 1
    n = int(raw_input())
    lis=[]
    for i in range(2*n):
        lis.append(map(int,raw_input().split(" ")))
    sumi=0
    n=2*n
    for i in range(n/2):
        for j in range(n/2):
            sumi+=max(lis[i][j],lis[n-i-1][j],lis[i][n-1-j],lis[n-i-1][n-1-j])
    print sumi