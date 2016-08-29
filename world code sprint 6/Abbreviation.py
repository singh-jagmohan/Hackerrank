t = int(raw_input())
while t:
    t -= 1
    S1= raw_input()
    S2= raw_input()
    j = 0
    flag=0
    matched=[]
    for i in range(len(S1)):
        if S1[i].isupper():
            while j>=0:
                if j==len(S2):
                    j -=1
                if S1[i]==S2[j]:
                    if len(matched)>1:
                        matched.pop()
                    matched.append([i,1])
                    j +=1
                    break
                else:
                    j -= 1
                    if len(matched)>1:
                        if matched[-1][1]==0:
                            matched.pop()
                        else:
                            flag=1
                            break
        else:
            if j<len(S2):
                if S1[i].upper()==S2[j]:
                    matched.append([i, 0])
                    j +=1

        #print i
    if flag==0 and len(S2)==j:
        print "YES"
    else:
        print "NO"





