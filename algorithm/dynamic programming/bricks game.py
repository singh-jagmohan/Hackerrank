t = int(raw_input())
while t:
    t -= 1
    n = int(raw_input())
    lis = map(int,raw_input().split(" "))
    i = 0
    turn = 0
    score = 0
    while i<n:
        sumi = 0
        if n-i>5:
            a=sum(lis[i:i+3])-sum(lis[i+3:i+6])
            b=sum(lis[i:i+2])-sum(lis[i+2:i+5])
            c=sum(lis[i:i+1])-sum(lis[i+1:i+4])
            if a>=b and a>=c:
                sumi = sum(lis[i:i+3])
                i +=3
            elif b>=a and b>=c:
                sumi = sum(lis[i:i+2])
                i +=2
            elif c>=a and c>=b:
                sumi = sum(lis[i:i+1])
                i +=1

            turn = 1^turn
        elif n-i == 5:
            a=sum(lis[i:i+3])-sum(lis[i+3:])
            b=sum(lis[i:i+2])-sum(lis[i+2:])
            c=sum(lis[i:i+1])-sum(lis[i+1:i+4])
            if a>=b and a>=c:
                sumi = sum(lis[i:i+3])
                i +=3
            elif b>=a and b>=c:
                sumi = sum(lis[i:i+2])
                i +=2
            elif c>=a and c>=b:
                sumi = sum(lis[i:i+1])
                i +=1
            turn = 1^turn
        else:
            sumi = sum(lis[i:i+3])
            i +=3
            turn = 1^turn
        if turn ==1:
            score += sumi

    print score