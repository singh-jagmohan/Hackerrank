import sys

n = int(raw_input())

s = raw_input()

maximum = 0
value = ''

def isValid(string):
    #print string
    if len(string)==0:
        return False
    check = string[0]
    for i in string[1:]:
        if i ==check:
            return False
        else:
            check = i
    return True

if n ==1:
    print 0
else:
    for i in range(25):
        char1 = chr(i+97)
        for j in range(i+1,26):
            char2 = chr(j+97)
            c = s
            # print "c: ",c
            whitelist = set([char1,char2])
            #print "white: ", whitelist
            answer = ''.join(filter(whitelist.__contains__, c))
            # print answer
            # print char2
            # print char1
            # sys.exit()
            if isValid(answer) and len(answer)>maximum:
                maximum = len(answer)
                value = answer
                #print "here"

    print maximum
    #print value