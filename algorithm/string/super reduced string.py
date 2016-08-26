# Enter your code here. Read input from STDIN. Print output to STDOUT
s = raw_input()
while 1:
    n = len(s)
    flag = 0
    for i in range(1, n):
        if s[i - 1] == s[i]:
            s = s[:i - 1] + s[i + 1:]
            flag = 1
            break
    if flag == 0:
        if len(s) == 0:
            print "Empty String"
        else:
            print s
        break
